def pre_init_hook(env):
    """Allow installing sale_quotation_builder in databases
    with large sale.order / sale.order.line tables.
    Since website_description fields computation is based
    on new fields added by the module, they will be empty anyway.
    By avoiding the computation of those fields,
    we reduce the installation time noticeably
    """

    def add_column_if_not_exists(table_name, column_name, column_type='text'):
        env.cr.execute("""
                       SELECT column_name
                       FROM information_schema.columns
                       WHERE table_name = %s
                         AND column_name = %s
                       """, (table_name, column_name))

        if not env.cr.fetchone():
            env.cr.execute(f"""
                ALTER TABLE "{table_name}"
                ADD COLUMN "{column_name}" {column_type}
            """)

    # Add website_description columns to all required tables
    add_column_if_not_exists('sale_order', 'website_description')
    add_column_if_not_exists('sale_order_line', 'website_description')
    add_column_if_not_exists('sale_order_template_line', 'website_description')
    add_column_if_not_exists('sale_order_template_option', 'website_description')