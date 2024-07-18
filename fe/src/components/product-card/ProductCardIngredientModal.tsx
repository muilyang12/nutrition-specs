"use client";

import { useEffect, useState } from "react";
import { useIngredientsStore } from "@stores/apiResponse/ingredientsStore";
import { foodApi } from "@apis/food";
import styles from "./ProductCardIngredientModal.module.css";

interface Props {
  productName: string;
  s3Key: string;
  ingredientIds: number[];
}

export default function ProductCardIngredientModal(props: Props) {
  const { productName, s3Key, ingredientIds } = props;

  const { ingredientRecord, addIngredientRecord } = useIngredientsStore();

  const [ingredientsData, setIngredientsData] = useState<Record<number, [string, string]>>({});
  useEffect(() => {
    const newIngredientIds: number[] = [];

    const newIngredientsData: Record<number, [string, string]> = {};

    ingredientIds.forEach((ingredientId) => {
      if (ingredientId in ingredientRecord) {
        const [ingredientName, ingredientExplanation] = ingredientRecord[ingredientId];
        newIngredientsData[ingredientId] = [ingredientName, ingredientExplanation];
      } else {
        newIngredientIds.push(ingredientId);
        newIngredientsData[ingredientId] = ["", ""];
      }
    });

    foodApi.getIngredients(newIngredientIds).then((newIngredients) => {
      newIngredients.forEach((newIngredient) => {
        const { id, name, description } = newIngredient;

        addIngredientRecord(id, name, description);
        newIngredientsData[id] = [name, description];
      });
    });

    setIngredientsData(newIngredientsData);
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
