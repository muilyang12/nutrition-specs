import { create } from "zustand";
import { ProductNutritionResult } from "@apis/food.define";

interface ComparingProducts {
  comparingProducts: Record<string, ProductNutritionResult>;
  setComparingProducts: (newProductNutritions: Record<string, ProductNutritionResult>) => void;
}

export const useComparingProductsStore = create<ComparingProducts>()((set) => ({
  comparingProducts: {},
  setComparingProducts: (newProductNutritions: Record<string, ProductNutritionResult>) =>
    set(() => ({ comparingProducts: newProductNutritions })),
}));
