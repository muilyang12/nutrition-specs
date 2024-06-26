export interface FoodCategoryRs {
  id: number;
  category_name: string;
  category_key: string;
}

export interface ProductRs {
  id: number;
  food_categories: number[];
  brand_name: string;
  product_name: string;
}

export interface NutritionRs {
  id: number;
  product: number;
  s3_url: string;
  data: NutritionData;
}

export interface NutritionData {
  serving_size: number;
  serving_unit: string;
  calories: number;
  sodium: number;
  total_carbohydrate: number;
  sugars: number;
  allulose: number;
  dietary_fiber: number;
  total_fat: number;
  trans_fat: number;
  saturated_fat: number;
  cholesterol: number;
  protein: number;
  calcium: number;
  iron: number;
  vitamin_A: number;
  vitamin_C: number;
}
