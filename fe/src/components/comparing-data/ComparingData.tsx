"use client";

import ComparingDataMainTable from "./ComparingDataMainTable";
import ComparingDataDetailTable from "./ComparingDataDetailTable";
import styles from "./ComparingData.module.css";

export default function ComparingData() {
  return (
    <>
      <div className={styles.comparingDataWrapper}>
        <span className={styles.comparingDataTitle}>Nutrition</span>

        <div className={styles.comparingDataParts}>
          <div className={styles.comparingDataPart}>
            <span className={styles.comparingDataPartTitle}>주요 영양소</span>
            <ComparingDataMainTable />
          </div>

          <div className={styles.comparingDataPart}>
            <span className={styles.comparingDataPartTitle}>상세</span>
            <ComparingDataDetailTable />
          </div>
        </div>
      </div>
    </>
  );
}
