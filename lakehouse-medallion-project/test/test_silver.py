def test_email_column_exists():

    assert "email" in df.columns


def test_customer_id_not_null():

    assert (
        df.filter(
            df.customer_id.isNull()
        ).count()
        == 0
    )