interface Params {
  [key: string]: string | string[];
}

export interface FoodCategoryPageParams extends Params {
  foodCategory: string;
}
