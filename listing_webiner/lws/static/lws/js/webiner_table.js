var webiner_table_app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#webiner_table_app',
    data:{
        columns: [
        {
            label: '開催日時',
            field: 'date',
            width: '100px',
        },
        {
            label: 'タイトル',
        　  field: 'title',
        },
        {
            label: 'URL',
            field: 'url',
            hidden: true,
        },
        {
            label: 'カテゴリ',
            field: 'category',
            width: '100px',
        },
        ],
        searchOptions: {
            enabled: true,
            trigger: 'enter',
            skipDiacritics: false,
            placeholder: 'Webinerを検索します',
        }
    },
    methods: {
        onRowClick : function(params) {
            window.open(params.row['url'], '_blank');
        }
    }
});