"use client";

import { useModalStore } from "@stores/modalStore";
import styles from "./Modal.module.css";

export default function Modal() {
  const { modal, closeModal } = useModalStore();

  const handleClickGrayFilter = () => closeModal();

  return (
    <>
      {modal && (
        <div className={styles.modalWrapper}>
          <div className={styles.modalContent}>{modal}</div>
          <div className={styles.grayFilter} onClick={handleClickGrayFilter} />
        </div>
      )}
    </>
  );
}
