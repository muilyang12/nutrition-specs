import { ReactElement } from "react";
import { create } from "zustand";

interface ModalStore {
  modal: ReactElement | null;

  openModal: (newModal: ReactElement) => void;
  closeModal: () => void;
}

export const useModalStore = create<ModalStore>()((set) => ({
  modal: null,

  openModal: (newModal: ReactElement) => set({ modal: newModal }),
  closeModal: () => set({ modal: null }),
}));
