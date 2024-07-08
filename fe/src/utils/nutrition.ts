import { NUTRITION_KEY_UNIT_MAPPER, NutritionDataKey } from "@defines/nutrition";

export const getNutritionWithUnit = (key: NutritionDataKey, value?: number) => {
  if (!value) return "";

  if (key === "calories") return `${value} ${NUTRITION_KEY_UNIT_MAPPER[key]}`;
  else return `${value}${NUTRITION_KEY_UNIT_MAPPER[key]}`;
};
