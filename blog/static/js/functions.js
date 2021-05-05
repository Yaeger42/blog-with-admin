function showLoading() {
    return $.dialog({
        closeIcon: false,
        title: false,
        columnClass: 'xsmall',
        content: '<div class="text-center"><i class="fas fa-spinner fa-pulse mr-2"></i>Loading...</div>'
    });
}