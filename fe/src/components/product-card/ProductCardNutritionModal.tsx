"use client";

import styles from "./ProductCardNutritionModal.module.css";

interface Props {
  productName: string;
  s3Key: string;
}

export default function ProductCardNutritionModal(props: Props) {
  const { productName, s3Key } = props;

  return (
    <div className={styles.modalWrapper}>
      <img
        src={`https://static.nutrition-specs.com/${encodeURIComponent(s3Key)}`}
        alt={productName}
      />
    </div>
  );
}
