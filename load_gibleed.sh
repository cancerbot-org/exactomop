
for f in ./data/GiBleed/GiBleed_5.3/CONDITION_OCCURRENCE.csv; do
    file_name=$(basename "$f" .csv)
    # Convert file_name (e.g., PERSON) to PascalCase (e.g., Person)
    model_name=$(echo "$file_name" | awk -F'_' '{for(i=1;i<=NF;i++){printf toupper(substr($i,1,1)) tolower(substr($i,2))}}')
    echo "Loading $model_name from $f"
    python manage.py load_csv_to_model "$model_name" "$f"
    echo "Done loading $model_name"
done