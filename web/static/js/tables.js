pyt= {
    frame_table: function() {
        return $('.frame').DataTable({
                "info": false,
                "bPaginate": false,
                "paging": false,
                "bScrollCollapse": false,
                "search": true,
                "sort": true,
                "filter": true,
                dom: 'T<"clear">lfrtip',
                "tableTools": {
                    "sSwfPath": "/static/js/swf/copy_csv_xls_pdf.swf"
                }
            });
    }
};
