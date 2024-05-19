import { axiosInstance } from "./axiosInstance";
import { FoodCategoryRs, NutritionRs, ProductRs } from "./food.define";

export const foodApi = {
  getFoodCategories: async () =>
    (await axiosInstance.get<FoodCategoryRs[]>("food/food-category/")).data,
  getProducts: async (foodCategoryId: number) =>
    (await axiosInstance.get<ProductRs[]>(`food/product/?food-category=${foodCategoryId}`)).data,
  getNutritions: async (productId: number) =>
    (await axiosInstance.get<NutritionRs[]>(`food/nutrition/?product=${productId}`)).data,
};
