import { ReactNode } from "react";
import { CircularProgress } from "@mui/material";
import styles from "./LoadingSpinner.module.css";

interface Props {
  isLoadingDone?: boolean;
  height?: number;
  size?: number;
  children: ReactNode;
}

export default function LoadingSpinner(props: Props) {
  const { isLoadingDone, height = 80, size = 50, children } = props;

  if (isLoadingDone) return children;
  else
    return (
      <div className={styles.loadingSpinnerWrapper} style={{ height: `${height}px` }}>
        <CircularProgress color="inherit" size={size} />
      </div>
    );
}
