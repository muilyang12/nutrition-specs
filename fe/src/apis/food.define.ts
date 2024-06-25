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
  data: Record<string, string>;
}
