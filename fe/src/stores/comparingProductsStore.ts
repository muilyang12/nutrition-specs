import { create } from "zustand";
import { ProductDetailResult } from "@apis/food.define";

interface ComparingProducts {
  comparingProducts: Record<string, ProductDetailResult>;
  setComparingProducts: (newProductNutritions: Record<string, ProductDetailResult>) => void;
}

export const useComparingProductsStore = create<ComparingProducts>()((set) => ({
  comparingProducts: {},
  setComparingProducts: (newProductNutritions: Record<string, ProductDetailResult>) =>
    set(() => ({ comparingProducts: newProductNutritions })),
}));
