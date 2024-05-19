export interface FoodCategoryRs {
  id: number;
  category_name: string;
}

export interface ProductRs {
  id: number;
  food_category: number;
  brand_name: string;
  product_name: string;
}

export interface NutritionRs {
  id: number;
  product: number;
  serving_size: number;
  calory: number;
  carbohydrate: number;
  protein: number;
  fat: number;
}
