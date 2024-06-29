import { create } from "zustand";

interface BrandFilterStore {
  selectedFilters: string[];
  setSelectedFilters: (newFilters: string[]) => void;
  addSelectedFilter: (newFilter: string) => void;
  deleteSelectedFilter: (targetFilter: string) => void;
}

export const useBrandFilterStore = create<BrandFilterStore>()((set) => ({
  selectedFilters: [],
  setSelectedFilters: (newFilters: string[]) => set(() => ({ selectedFilters: newFilters })),
  addSelectedFilter: (newFilter: string) =>
    set((state) => ({ selectedFilters: [...state.selectedFilters, newFilter] })),
  deleteSelectedFilter: (targetFilter: string) =>
    set((state) => ({
      selectedFilters: state.selectedFilters.filter((brandName) => brandName !== targetFilter),
    })),
}));
