export type NutritionKey =
  | "calories"
  | "sodium"
  | "total_carbohydrate"
  | "sugars"
  | "allulose"
  | "dietary_fiber"
  | "total_fat"
  | "trans_fat"
  | "saturated_fat"
  | "cholesterol"
  | "protein"
  | "calcium"
  | "iron"
  | "vitamin_A"
  | "vitamin_C";

export const NUTRITION_KEY_NAME_MAPPER: Record<NutritionKey, string> = {
  calories: "열량",
  sodium: "나트륨",
  total_carbohydrate: "탄수화물",
  sugars: "당류",
  allulose: "알룰로스",
  dietary_fiber: "식이섬유",
  total_fat: "지방",
  trans_fat: "트랜스지방",
  saturated_fat: "포화지방",
  cholesterol: "콜레스테롤",
  protein: "단백질",
  calcium: "칼슘",
  iron: "철분",
  vitamin_A: "비타민A",
  vitamin_C: "비타민C",
};

export const NUTRITION_KEY_UNIT_MAPPER: Record<NutritionKey, string> = {
  calories: "kcal",
  sodium: "mg",
  total_carbohydrate: "g",
  sugars: "g",
  allulose: "g",
  dietary_fiber: "g",
  total_fat: "g",
  trans_fat: "g",
  saturated_fat: "g",
  cholesterol: "mg",
  protein: "g",
  calcium: "mg",
  iron: "mg",
  vitamin_A: "mg",
  vitamin_C: "mg",
};
