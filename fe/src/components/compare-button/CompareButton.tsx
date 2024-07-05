"use client";

import { useRouter } from "next/navigation";
import CloseIcon from "@mui/icons-material/Close";
import ArrowForwardIcon from "@mui/icons-material/ArrowForward";
import qs from "qs";
import { useCompareStore } from "@stores/compareStore";
import styles from "./CompareButton.module.css";

export default function CompareButton() {
  const router = useRouter();

  const { isComparing, toggleIsComparing, selectedProducts, resetState } = useCompareStore();

  const handleClickGotoButton = () => {
    const queries = qs.stringify(
      {
        product: selectedProducts,
      },
      { arrayFormat: "repeat" }
    );

    router.push(`/compare?${queries}`);

    setTimeout(() => {
      resetState();
    }, 500);
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
            <CloseIcon fontSize="small" />
          </button>
          <button
            className={`${styles.gotoButton} ${selectedProducts.length < 2 ? styles.disabled : ""}`}
            onClick={handleClickGotoButton}
          >
            <ArrowForwardIcon fontSize="small" />
          </button>
        </>
      )}
    </div>
  );
}
