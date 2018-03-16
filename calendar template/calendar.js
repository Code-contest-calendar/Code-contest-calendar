$(function () {

    var now = new Date();

    $('#demo').mobiscroll().eventcalendar({
        theme: 'ios',
        display: 'center',
        layout: 'liquid',
        firstDay: 1,
        yearChange: true,
        calendarScroll: 'horizontal',
        showOuterDays: true,
        showEventCount: true,
        data: [{
            d: new Date(now.getFullYear(), now.getMonth(), 8, 8, 0),
            text: 'Green box to post office',
            color: '#6e7f29'
        }, {
            d: new Date(now.getFullYear(), now.getMonth(), 8, 8, 45),
            text: 'Quick mtg. with Martin',
            color: '#de3d83'
        }, {
            d: new Date(now.getFullYear(), now.getMonth(), 8, 9, 30),
            text: 'Product team mtg.',
            color: '#f67944'
        }, {
            d: new Date(now.getFullYear(), now.getMonth(), 8, 11, 0),
            text: 'Stakeholder mtg.',
            color: '#f67944'
        }, {
            d: new Date(now.getFullYear(), now.getMonth(), 8, 12, 30),
            text: 'Lunch @ Butcher\'s',
            color: '#00aabb'
        }, {
            d: new Date(now.getFullYear(), now.getMonth(), 8, 15, 0),
            text: 'General orientation',
            color: '#f67944'
        }, {
            d: (now.getMonth() + 1) + '/14',
            text: 'Dexter BD',
            color: '#37bbe4'
        }, {
            d: (now.getMonth() + 1) + '/5',
            text: 'Luke BD',
            color: '#37bbe4'
        }, {
            d: 'w3',
            text: 'Employment (Semi-weekly)',
            color: '#635045'
        }, {
            d: 'w5',
            text: 'Employment (Semi-weekly)',
            color: '#635045'
        }, {
            start: new Date(now.getFullYear(), now.getMonth(), 26),
            end: new Date(now.getFullYear(), now.getMonth(), 31),
            text: 'Dean OFF',
            color: '#e7b300'
        }, {
            start: new Date(now.getFullYear(), (now.getMonth() + 1), 5),
            end: new Date(now.getFullYear(), (now.getMonth() + 1), 14),
            text: 'Mike OFF',
            color: '#e7b300'
        }, {
            d: '11/2',
            text: 'File Form 720 for the third quarter',
            color: '#a63e14'
        }, {
            d: '11/2',
            text: 'File Form 730 and pay tax on wagers accepted during September',
            color: '#a63e14'
        }, {
            d: '11/2',
            text: 'File Form 2290 and pay the tax for vehicles first used during September',
            color: '#a63e14'
        }, {
            d: '11/2',
            text: 'File Form 941 for the third quarter',
            color: '#a63e14'
        }, {
            d: '11/2',
            text: 'Deposit FUTA owed through Sep if more than $500',
            color: '#a63e14'
        }, {
            d: '11/30',
            text: 'Deposit payroll tax for payments on Nov 21-24 if the semiweekly deposit rule applies',
            color: '#a63e14'
        }, {
            d: '11/30',
            text: 'File Form 730 and pay tax on wagers accepted during October',
            color: '#a63e14'
        }, {
            d: '11/30',
            text: 'File Form 2290 and pay the tax for vehicles first used during October',
            color: '#a63e14'
        }]

    });

    $('#show').click(function () {
        $('#demo').mobiscroll('show');
        return false;
    });

});
