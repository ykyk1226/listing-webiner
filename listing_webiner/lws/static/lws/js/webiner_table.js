var selected_rows;

new Vue({
    delimiters: ['[[', ']]'],
    el: '#webiner_table_app',
    data:{
        columns: [
        {
            label: 'ID',
            field: 'id',
            hidden: true,
        },
        {
            label: '開催日時',
            field: 'start_date',
            width: '100px',
            thClass: 'th-date',
        },
        {
            label: '終了日時',
            field: 'end_date',
            width: '100px',
            thClass: 'th-date',
        },
        {
            label: 'タイトル',
        　  field: 'title',
            tdClass: 'cell-title',
        },
        {
            label: 'URL',
            field: 'url',
            hidden: true,
        },
        {
            label: 'カテゴリ',
            field: 'category',
            width: '150px',
            filterOptions: {
                enabled: true,
                placeholder: 'カテゴリで絞る',
                filterDropdownItems: category_list,
            },
        },
        ]
    },
    methods: {
        onCellClick : function(params) {
            if (params.column.field == 'title') {
                window.open(params.row['url'], '_blank');
            }
        },
        tableFilter : function(row, col, cellValue, searchTerm) {
            let table_filter = $("#table_filter option:selected").len;
            if (table_filter == 0) {
                return true;
            } else {
                return table_filter.indexOf(row['category']) >= 0;
            }
        },
        selectionChanged : function() {
            selected_rows = this.$refs['webiner_table'].selectedRows;
        },
    }
});

function delete_message() {
    document.getElementById("add_webiner_result_message").innerHTML = "";
    document.getElementById("batsu").innerHTML = "";
}