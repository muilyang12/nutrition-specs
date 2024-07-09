import qs from "qs";
import { axiosInstance } from "./axiosInstance";
import {
  FoodCategoryRs,
  NutritionRs,
  BrandRs,
  ProductRs,
  ProductNutritionRs,
  ProductNutritionResult,
} from "./food.define";

export const foodApi = {
  getAllFoodCategories: async () =>
    (await axiosInstance.get<FoodCategoryRs[]>("food/food-category/")).data,
  getMainFoodCategories: async () =>
    (await axiosInstance.get<FoodCategoryRs[]>("food/food-category/main")).data,
  getSubFoodCategories: async (mainCategoryKey: string) =>
    (await axiosInstance.get<FoodCategoryRs[]>(`food/food-category/sub/${mainCategoryKey}`)).data,
  getFoodCategoryByCategoryKey: async (categoryKey: string) =>
    (await axiosInstance.get<FoodCategoryRs>(`food/food-category/category-key/${categoryKey}/`))
      .data,
  getBrands: async (foodCategoryKey: string) =>
    (await axiosInstance.get<BrandRs[]>(`food/brand/?category-key=${foodCategoryKey}`)).data,
  getProducts: async (foodCategoryKey: string, brands?: string[]) => {
    const queries = qs.stringify(
      {
        "category-key": foodCategoryKey,
        brand: brands,
      },
      { arrayFormat: "repeat" }
    );

    return (await axiosInstance.get<ProductRs>(`food/product/?${queries}`)).data;
  },
  getNutritions: async (productIds: number[]) => {
    const queries = qs.stringify(
      {
        product: productIds,
      },
      { arrayFormat: "repeat" }
    );

    return (await axiosInstance.get<NutritionRs[]>(`food/nutrition/?${queries}`)).data;
  },
  getProductNutritions: async (foodCategoryKey: string, brands?: string[], page?: number) => {
    const queries = qs.stringify(
      {
        "category-key": foodCategoryKey,
        brand: brands,
        page: page,
      },
      { arrayFormat: "repeat" }
    );

    return (await axiosInstance.get<ProductNutritionRs>(`food/product-nutrition/?${queries}`)).data;
  },
  getProductNutrition: async (productId: number) =>
    (await axiosInstance.get<ProductNutritionResult>(`food/product-nutrition/${productId}/`)).data,
};
