import { create } from "zustand";

interface CompareStore {
  isComparing: boolean;
  toggleIsComparing: () => void;
  selectedProducts: number[];
  toggleSelectedProduct: (newProductId: number) => void;
}

export const useCompareStore = create<CompareStore>()((set) => ({
  isComparing: false,
  toggleIsComparing: () => set((state) => ({ isComparing: !state.isComparing })),
  selectedProducts: [],
  toggleSelectedProduct: (newProductId: number) =>
    set((state) => ({
      selectedProducts: state.selectedProducts.includes(newProductId)
        ? state.selectedProducts.filter((id) => id !== newProductId)
        : [...state.selectedProducts, newProductId],
    })),
}));
