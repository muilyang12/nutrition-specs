import { create } from "zustand";

interface CompareStore {
  isComparing: boolean;
  toggleIsComparing: () => void;
  selectedProducts: number[];
  addSelectedProduct: (newProductId: number) => void;
  removeSelectedProduct: (newProductId: number) => void;
}

export const useCompareStore = create<CompareStore>()((set) => ({
  isComparing: false,
  toggleIsComparing: () => set((state) => ({ isComparing: !state.isComparing })),
  selectedProducts: [],
  addSelectedProduct: (newProductId: number) =>
    set((state) => ({ selectedProducts: [...state.selectedProducts, newProductId] })),
  removeSelectedProduct: (newProductId: number) =>
    set((state) => ({
      selectedProducts: state.selectedProducts.filter((id) => id !== newProductId),
    })),
}));
