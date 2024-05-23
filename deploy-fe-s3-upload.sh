#!/bin/bash

SOURCE_DIR="./fe/dist"
S3_BUCKET="s3://muilyang12-nutrition-comparison-fe"

echo "Uploading files in $SOURCE_DIR to $S3_BUCKET"
for FILE_PATH in "$SOURCE_DIR"/*; do
    FILE_NAME=$(basename "$FILE_PATH")
    
    if [[ "$FILE_NAME" == *.html ]]; then
        FILE_BASE_NAME="${FILE_NAME%.html}"
        S3_PATH="$S3_BUCKET/$FILE_BASE_NAME"
    else
        S3_PATH="$S3_BUCKET/$FILE_NAME"
    fi

    /mnt/c/Program\ Files/Amazon/AWSCLIV2/aws.exe s3 cp "$FILE_PATH" "$S3_PATH"
done