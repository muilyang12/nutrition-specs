"use client";

import { useEffect, useState } from "react";
import { useIngredientsStore } from "@stores/apiResponse/ingredientsStore";
import styles from "./ProductCardIngredientModal.module.css";

interface Props {
  productName: string;
  s3Key: string;
  ingredientIds: number[];
}

export default function ProductCardIngredientModal(props: Props) {
  const { productName, s3Key, ingredientIds } = props;

  const { ingredientRecord, addIngredientRecord } = useIngredientsStore();

  const [ingredienData, setIngredienData] = useState<Record<string, string>>({});
  useEffect(() => {
    ingredientIds.forEach((ingredientId) => {
      if (ingredientId in ingredientRecord) {
        const [ingredientName, ingredientExplanation] = ingredientRecord[ingredientId];
        setIngredienData((prev) => ({ ...prev, [ingredientName]: ingredientExplanation }));
      } else {
        // API 호출부분 추가.
      }
    });
  }, [ingredientIds]);

  return (
    <div className={styles.modalWrapper}>
      <img
        src={`https://static.nutrition-specs.com/${encodeURIComponent(s3Key)}`}
        alt={productName}
      />
    </div>
  );
}
