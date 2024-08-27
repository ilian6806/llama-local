
if [ -z "$1" ]
then
    echo "No model privided"
    exit 1
fi

echo "Preloading model $1..."

curl -X POST http://localhost:11434/api/generate -d "{\"model\": \"$1\", \"keep_alive\": -1}"

echo ""
echo "Model $1 preloaded."
