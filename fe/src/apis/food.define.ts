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
  s3_key: string;
  data: NutritionData;
}

export interface IngredientRs {
export interface ProductIngredientRs {
  id: number;
  product: number;
  ingredients: number[];
  s3_key: string;
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

export interface ProductDetailResult extends ProductResult {
  nutritions: NutritionRs[];
  ingredients: ProductIngredientRs[];
}
export type ProductDetailRs = RsWithPagination<ProductDetailResult>;
