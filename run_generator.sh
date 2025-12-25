#!/bin/bash

# =============================================================================
# Test Case Generator - Run Script
# =============================================================================

# Configuration
API_KEY="${OPENROUTER_API_KEY:-}"  # Set via environment or edit below
MODEL="${MODEL:-google/gemini-2.0-flash-exp:free}"

# Available free models:
#   google/gemini-2.0-flash-exp:free
#   meta-llama/llama-3.2-3b-instruct:free
#
# Available paid models:
#   openai/gpt-4o
#   openai/gpt-4o-mini
#   anthropic/claude-3.5-sonnet
#   google/gemini-pro

# =============================================================================
# DO NOT EDIT BELOW THIS LINE (unless you know what you're doing)
# =============================================================================

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Default values
INPUT_FILE=""
CREDENTIALS_FILE=""
OUTPUT_DIR="output"
DEBUG_MODE=false

# Print usage
usage() {
    echo -e "${BLUE}Usage:${NC} $0 [OPTIONS]"
    echo ""
    echo -e "${YELLOW}Required:${NC}"
    echo "  -i, --input FILE       Path to functional description JSON"
    echo "  -k, --api-key KEY      OpenRouter API key (or set OPENROUTER_API_KEY env var)"
    echo ""
    echo -e "${YELLOW}Optional:${NC}"
    echo "  -c, --credentials FILE Path to credentials JSON"
    echo "  -o, --output DIR       Output directory (default: output)"
    echo "  -m, --model MODEL      Model to use (default: google/gemini-2.0-flash-exp:free)"
    echo "  -d, --debug            Enable debug mode (logs to debug_log.txt)"
    echo "  -h, --help             Show this help message"
    echo ""
    echo -e "${YELLOW}Examples:${NC}"
    echo "  $0 -i functional_desc.json -k sk-or-v1-xxx"
    echo "  $0 -i functional_desc.json -k sk-or-v1-xxx -m openai/gpt-4o -d"
    echo "  $0 -i functional_desc.json -c credentials.json -o my_output -d"
    echo ""
    echo -e "${YELLOW}Environment Variables:${NC}"
    echo "  OPENROUTER_API_KEY     API key (alternative to -k flag)"
    echo "  MODEL                  Model identifier (alternative to -m flag)"
    exit 1
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -i|--input)
            INPUT_FILE="$2"
            shift 2
            ;;
        -k|--api-key)
            API_KEY="$2"
            shift 2
            ;;
        -c|--credentials)
            CREDENTIALS_FILE="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -m|--model)
            MODEL="$2"
            shift 2
            ;;
        -d|--debug)
            DEBUG_MODE=true
            shift
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo -e "${RED}Error:${NC} Unknown option $1"
            usage
            ;;
    esac
done

# Validate required arguments
if [[ -z "$INPUT_FILE" ]]; then
    echo -e "${RED}Error:${NC} Input file is required (-i)"
    usage
fi

if [[ -z "$API_KEY" ]]; then
    echo -e "${RED}Error:${NC} API key is required (-k or OPENROUTER_API_KEY env var)"
    usage
fi

if [[ ! -f "$INPUT_FILE" ]]; then
    echo -e "${RED}Error:${NC} Input file not found: $INPUT_FILE"
    exit 1
fi

if [[ -n "$CREDENTIALS_FILE" && ! -f "$CREDENTIALS_FILE" ]]; then
    echo -e "${RED}Error:${NC} Credentials file not found: $CREDENTIALS_FILE"
    exit 1
fi

# Build command
CMD="python -m test_case_generator.main --generate"
CMD+=" --input \"$INPUT_FILE\""
CMD+=" --api-key \"$API_KEY\""
CMD+=" --model \"$MODEL\""
CMD+=" --output \"$OUTPUT_DIR\""

if [[ -n "$CREDENTIALS_FILE" ]]; then
    CMD+=" --credentials \"$CREDENTIALS_FILE\""
fi

if [[ "$DEBUG_MODE" == true ]]; then
    CMD+=" --debug"
fi

# Print configuration
echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}   Test Case Generator${NC}"
echo -e "${BLUE}============================================${NC}"
echo -e "${GREEN}Input:${NC}       $INPUT_FILE"
if [[ -n "$CREDENTIALS_FILE" ]]; then
    echo -e "${GREEN}Credentials:${NC} $CREDENTIALS_FILE"
fi
echo -e "${GREEN}Output:${NC}      $OUTPUT_DIR"
echo -e "${GREEN}Model:${NC}       $MODEL"
echo -e "${GREEN}Debug:${NC}       $DEBUG_MODE"
echo -e "${BLUE}============================================${NC}"
echo ""

# Change to script directory and run
cd "$SCRIPT_DIR"
echo -e "${YELLOW}Running...${NC}"
echo ""

eval $CMD
EXIT_CODE=$?

echo ""
if [[ $EXIT_CODE -eq 0 ]]; then
    echo -e "${GREEN}============================================${NC}"
    echo -e "${GREEN}   Generation Complete!${NC}"
    echo -e "${GREEN}============================================${NC}"
    echo -e "Output files:"
    echo -e "  - ${BLUE}$OUTPUT_DIR/test-cases.json${NC}"
    echo -e "  - ${BLUE}$OUTPUT_DIR/navigation_graph.png${NC}"
    if [[ "$DEBUG_MODE" == true ]]; then
        echo -e "  - ${BLUE}debug_log.txt${NC}"
    fi
else
    echo -e "${RED}============================================${NC}"
    echo -e "${RED}   Generation Failed (exit code: $EXIT_CODE)${NC}"
    echo -e "${RED}============================================${NC}"
    if [[ "$DEBUG_MODE" == true ]]; then
        echo -e "Check ${BLUE}debug_log.txt${NC} for details"
    else
        echo -e "Run with ${YELLOW}-d${NC} flag for debug output"
    fi
fi

exit $EXIT_CODE


#   export OPENROUTER_API_KEY="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"
#   export MODEL="google/gemini-2.5-pro"
#   ./run_generator.sh -i functional_desc.json -d
