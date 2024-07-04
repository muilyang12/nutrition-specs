"use client";

import { useRouter } from "next/navigation";
import qs from "qs";
import { useCompareStore } from "@stores/compareStore";
import styles from "./CompareButton.module.css";

export default function CompareButton() {
  const router = useRouter();

  const { isComparing, toggleIsComparing, selectedProducts } = useCompareStore();

  const handleClickGotoButton = () => {
    const queries = qs.stringify(
      {
        product: selectedProducts,
      },
      { arrayFormat: "repeat" }
    );

    router.push(`/compare?${queries}`);
  };

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
            onClick={handleClickGotoButton}
          >
            →
          </button>
        </>
      )}
    </div>
  );
}
