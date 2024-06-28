import { axiosInstance } from "./axiosInstance";
import { FoodCategoryRs, NutritionRs, BrandRs, ProductRs } from "./food.define";

export const foodApi = {
  getFoodCategories: async () =>
    (await axiosInstance.get<FoodCategoryRs[]>("food/food-category/")).data,
  getFoodCategoryByCategoryKey: async (categoryKey: string) =>
    (await axiosInstance.get<FoodCategoryRs>(`food/food-category/category-key/${categoryKey}/`))
      .data,
  getBrands: async (foodCategoryKey: string) =>
    (await axiosInstance.get<BrandRs[]>(`food/brand/?category-key=${foodCategoryKey}`)).data,
  getProducts: async (foodCategoryKey: string) =>
    (await axiosInstance.get<ProductRs>(`food/product/?category-key=${foodCategoryKey}`)).data,
  getNutritions: async (productIds: number[]) => {
    const queries = productIds.map((id) => `product=${id}`).join("&");

    return (await axiosInstance.get<NutritionRs[]>(`food/nutrition/?${queries}`)).data;
  },
};
