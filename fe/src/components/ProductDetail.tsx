"use client";

import { useEffect, useState } from "react";
import { foodApi } from "@apis/food";
import { NutritionRs } from "@apis/food.define";

interface Props {
  productId: number;
}

export default function ProductDetail(props: Props) {
  const { productId } = props;

  const [nutrition, setNutrition] = useState<NutritionRs>();

  useEffect(() => {
    if (!productId) return;

    foodApi.getNutritions(productId).then((data) => setNutrition(data[0]));
  }, [productId]);

  if (!nutrition) return <></>;

  return (
    <>
      <div>calory: {nutrition.calory}</div>
      <div>carbohydrate: {nutrition.carbohydrate}</div>
      <div>protein: {nutrition.protein}</div>
      <div>fat: {nutrition.fat}</div>
    </>
  );
}
