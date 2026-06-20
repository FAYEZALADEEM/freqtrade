#!/bin/bash
# تشغيل متوازي لكل الاستراتيجيات — مُحسَّن لـ 32 vCPU / 128GB RAM
# الاستخدام: ./run_parallel.sh [--timerange YYYYMMDD-YYYYMMDD] [--jobs N] [--normal] [--freqai]
# مثال:      ./run_parallel.sh --timerange 20240101-20251231

set -e

TIMERANGE="${TIMERANGE:-20240101-20251231}"
NORMAL_JOBS="${NORMAL_JOBS:-32}"     # 59 استراتيجية عادية، 32 في آن واحد
FREQAI_JOBS="${FREQAI_JOBS:-9}"      # 9 استراتيجيات FreqAI كلها دفعة واحدة (كل منها n_jobs=3)
RESULTS_DIR="user_data/backtest_results"
LOGS_DIR="user_data/logs"
CONFIG_NORMAL="user_data/config_backtest.json"
CONFIG_FREQAI="user_data/config_freqai.json"

while [[ $# -gt 0 ]]; do
    case $1 in
        --timerange)    TIMERANGE="$2";     shift 2 ;;
        --jobs)         NORMAL_JOBS="$2";   shift 2 ;;
        --freqai-jobs)  FREQAI_JOBS="$2";   shift 2 ;;
        --normal)       RUN_NORMAL=1;       shift ;;
        --freqai)       RUN_FREQAI=1;       shift ;;
        *) echo "خيار غير معروف: $1"; exit 1 ;;
    esac
done

if [[ -z "$RUN_NORMAL" && -z "$RUN_FREQAI" ]]; then
    RUN_NORMAL=1
    RUN_FREQAI=1
fi

mkdir -p "$RESULTS_DIR" "$LOGS_DIR"

# إصلاح race condition — إنشاء المجلدات قبل التشغيل المتوازي
[ -f user_data/freqaimodels ] && rm -f user_data/freqaimodels
mkdir -p user_data/notebooks \
         user_data/plot \
         user_data/freqaimodels \
         user_data/hyperopts \
         user_data/hyperopt_results \
         user_data/logs

TOTAL_CPU=$(nproc)
TOTAL_MEM=$(free -g | awk '/^Mem:/{print $2}')

echo "=============================================="
echo "  Freqtrade Parallel Backtest"
echo "  Server    : ${TOTAL_CPU} vCPU / ${TOTAL_MEM}GB RAM"
echo "  Timerange : $TIMERANGE"
echo "  Normal jobs : $NORMAL_JOBS  |  FreqAI jobs: $FREQAI_JOBS"
echo "=============================================="

NORMAL_STRATEGIES=(
    BBMA_Engulfing_Riyadh_Strategy
    BreakerBlock_Retest
    CRT_1AM
    CRT_ThickCandleBreak
    FVG_Inversion_Trade
    ICT_SilverBullet_FVG
    LIB_STR003
    LIB_STR005
    LIB_STR005_EMA
    LIB_STR006
    LIB_STR007
    LIB_STR008
    LIB_STR011
    LIB_STR012
    LIB_STR012_BBMA
    LIB_STR013
    LIB_STR016
    LIB_STR026
    LIB_STR027
    LIB_STR027_VF
    LIB_STR027_Volume
    LIB_STR027_Volume_Fib_EMA
    LIB_STR029
    LIB_STR030
    LIB_STR039
    LIB_STR040
    LIB_STR042
    LIB_STR045
    LIB_STR047
    LIB_STR048
    LIB_STR051
    LIB_STR053
    LIB_STR054
    LIB_STR056
    LIB_STR057
    LIB_STR058
    LIB_STR060
    LIB_STR061
    LIB_STR062
    LIB_STR065
    LIB_STR068
    LIB_STR069
    LIB_STR071
    LIB_STR072
    LIB_STR073
    LIB_STR074
    MA_Pullback_Strategy
    MAPullbackTrendFollowing
    MAPullbackTrend
    OneHourForexReversal
    OpeningRangeBreakout
    ORB_Strategy
    RSI_Divergence_Reversal
    SMC_ICT_High_Frequency_Engine
    SMC_ICT_Riyadh
    SMC_LiquidityGrab_ImbalanceOB
    SMC_OrderBlock_BOS
    VSAConservativeTemplate
    VWAPPullback
)

FREQAI_STRATEGIES=(
    LIB_STR003_FreqAI
    LIB_STR005_FreqAI
    LIB_STR005_EMA_FreqAI
    LIB_STR007_FreqAI
    LIB_STR012_FreqAI
    LIB_STR013_FreqAI
    LIB_STR026_FreqAI
    LIB_STR030_FreqAI
    LIB_STR045_FreqAI
)

run_normal() {
    local strat="$1"
    local logfile="$LOGS_DIR/${strat}.log"
    local outfile="$RESULTS_DIR/${strat}"
    echo "[$(date +%H:%M:%S)] START  $strat"
    freqtrade backtesting \
        --config "$CONFIG_NORMAL" \
        --strategy "$strat" \
        --timerange "$TIMERANGE" \
        --export trades \
        --export-filename "${outfile}.json" \
        --cache none \
        > "$logfile" 2>&1 \
        && echo "[$(date +%H:%M:%S)] OK     $strat" \
        || echo "[$(date +%H:%M:%S)] FAIL   $strat → $logfile"
}

run_freqai() {
    local strat="$1"
    local logfile="$LOGS_DIR/${strat}.log"
    local outfile="$RESULTS_DIR/${strat}"
    # config خاص بكل استراتيجية مع identifier فريد لتجنّب تصادم مجلدات النماذج
    local cfg="/tmp/cfg_${strat}.json"
    sed "s|\"identifier\": *\"[^\"]*\"|\"identifier\": \"fai_${strat,,}\"|" "$CONFIG_FREQAI" > "$cfg"
    echo "[$(date +%H:%M:%S)] START  $strat [FreqAI]"
    freqtrade backtesting \
        --config "$cfg" \
        --strategy "$strat" \
        --timerange "$TIMERANGE" \
        --export trades \
        --export-filename "${outfile}.json" \
        --cache none \
        --freqaimodel LightGBMRegressor \
        > "$logfile" 2>&1 \
        && echo "[$(date +%H:%M:%S)] OK     $strat [FreqAI]" \
        || echo "[$(date +%H:%M:%S)] FAIL   $strat [FreqAI] → $logfile"
}

export -f run_normal run_freqai
export TIMERANGE CONFIG_NORMAL CONFIG_FREQAI RESULTS_DIR LOGS_DIR

START_TIME=$(date +%s)

if [[ "$RUN_NORMAL" == "1" ]]; then
    echo ""
    echo ">>> [$(date +%H:%M:%S)] تشغيل ${#NORMAL_STRATEGIES[@]} استراتيجية عادية (${NORMAL_JOBS} متوازية) ..."
    printf '%s\n' "${NORMAL_STRATEGIES[@]}" | xargs -P "$NORMAL_JOBS" -I{} bash -c 'run_normal "$@"' _ {}
    echo ">>> [$(date +%H:%M:%S)] انتهت الاستراتيجيات العادية."
fi

if [[ "$RUN_FREQAI" == "1" ]]; then
    echo ""
    echo ">>> [$(date +%H:%M:%S)] تشغيل ${#FREQAI_STRATEGIES[@]} استراتيجيات FreqAI (${FREQAI_JOBS} متوازية) ..."
    printf '%s\n' "${FREQAI_STRATEGIES[@]}" | xargs -P "$FREQAI_JOBS" -I{} bash -c 'run_freqai "$@"' _ {}
    echo ">>> [$(date +%H:%M:%S)] انتهت استراتيجيات FreqAI."
fi

END_TIME=$(date +%s)
ELAPSED=$(( END_TIME - START_TIME ))
MINUTES=$(( ELAPSED / 60 ))
SECONDS=$(( ELAPSED % 60 ))

echo ""
echo "=============================================="
echo "  اكتمل في ${MINUTES}m ${SECONDS}s"
echo "  النتائج في: $RESULTS_DIR"
echo "  شغّل: python3 collect_results.py"
echo "=============================================="
