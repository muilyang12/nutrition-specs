"use client";

import { useCompareStore } from "@stores/compareStore";
import styles from "./CompareButton.module.css";

export default function CompareButton() {
  const { toggleIsComparing } = useCompareStore();

  return (
    <button className={styles.compareButton} onClick={() => toggleIsComparing()}>
      Compare
    </button>
  );
}
