import cudf
import cupy as cp


def make_frame(ncols, nkey_cols, nrows, low=0, high=100):
    nval_cols = ncols - nkey_cols
    key_columns = {
        f"key{i}": cp.random.randint(low, high, nrows)
        for i in range(nkey_cols)
    }
    val_columns = {
        f"val{i}": cp.random.rand(nrows)
        for i in range(nval_cols)
    }
    return cudf.DataFrame({**key_columns, **val_columns})

def make_col(nrows, has_nulls=True):
    c = cudf.core.column.as_column(cp.random.randn(nrows))
    if has_nulls:
        c[::2] = None
    return c