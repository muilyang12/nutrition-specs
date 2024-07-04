"use client";

import { useCompareStore } from "@stores/compareStore";
import styles from "./CompareButton.module.css";

export default function CompareButton() {
  const { isComparing, toggleIsComparing, selectedProducts } = useCompareStore();
  return (
    <div className={styles.compareButtonWrapper}>
      {!isComparing ? (
        <button className={styles.compareButton} onClick={() => toggleIsComparing()}>
          Compare
        </button>
      ) : (
        <>
          <button className={styles.xButton} onClick={() => toggleIsComparing()}>
            X
          </button>
          <button
            className={`${styles.gotoButton} ${selectedProducts.length < 2 ? styles.disabled : ""}`}
          >
            →
          </button>
        </>
      )}
    </div>
  );
}
