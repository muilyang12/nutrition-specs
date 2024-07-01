export interface RsWithPagination<Result> {
  count: number;
  next: string;
  previous: string;
  results: Result[];
}

export interface FoodCategoryRs {
  id: number;
  category_name: string;
  category_key: string;
  parent_category: number;
}

export interface BrandRs {
  id: number;
  food_categories: number[];
  name: string;
}

export interface ProductResult {
  id: number;
  brand_name: string;
  product_name: string;
  coupang_url: string;
}
export type ProductRs = RsWithPagination<ProductResult>;

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

export interface ProductNutritionResult extends ProductResult {
  nutritions: NutritionRs[];
}
export type ProductNutritionRs = RsWithPagination<ProductNutritionResult>;
