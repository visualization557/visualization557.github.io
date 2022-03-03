

$(document).ready(function () {
    var sildeNum = $('.page').length,
        wrapperWidth = 100 * sildeNum,
        slideWidth = 100/sildeNum;
    $('.wrapper').width(wrapperWidth + '%');
    $('.page').width(slideWidth + '%');

    $('a.scrollitem').click(function(){
        $('a.scrollitem').removeClass('selected');
        $(this).addClass('selected');

        var slideNumber = $($(this).attr('href')).index('.page'),
            margin = slideNumber * -100 + '%';

        $('.wrapper').animate({marginLeft: margin},1000);
        return false;
    });
});

var employeeDetails = [
    "images/employee_details/Ada Campo-Corrente_details.png",
    "images/employee_details/Adan Morlun_details.png",
    "images/employee_details/Adra Nubarron_details.png",
    "images/employee_details/Albina Hafon_details.png",
    "images/employee_details/Anda Ribera_details.png",
    "images/employee_details/Axel Calzas_details.png",
    "images/employee_details/Benito Hawelon_details.png",
    "images/employee_details/Bertrand Ovan_details.png",
    "images/employee_details/Birgitta Frente_details.png",
    "images/employee_details/Brand Tempestad_details.png",
    "images/employee_details/Carla Forluniau_details.png",
    "images/employee_details/Cecilia Morluniau_details.png",
    "images/employee_details/Claudio Hawelon_details.png",
    "images/employee_details/Cornelia Lais_details.png",
    "images/employee_details/Dante Coginian_details.png",
    "images/employee_details/Dylan Scozzese_details.png",
    "images/employee_details/Edvard Vann_details.png",
    "images/employee_details/Elsa Orilla_details.png",
    "images/employee_details/Emile Arpa_details.png",
    "images/employee_details/Felix Balas_details.png",
    "images/employee_details/Felix Resumir_details.png",
    "images/employee_details/Gustav Cazar_details.png",
    "images/employee_details/Henk Mies_details.png",
    "images/employee_details/Hennie Osvaldo_details.png",
    "images/employee_details/Hideki Cocinaro_details.png",
    "images/employee_details/Inga Ferro_details.png",
    "images/employee_details/Ingrid Barranco_details.png",
    "images/employee_details/Irene Nant_details.png",
    "images/employee_details/Isak Baza_details.png",
    "images/employee_details/Isande Borrasca_details.png",
    "images/employee_details/Isia Vann_details.png",
    "images/employee_details/Kanon Herrero_details.png",
    "images/employee_details/Kare Orilla_details.png",
    "images/employee_details/Lars Azada_details.png",
    "images/employee_details/Lidelse Dedos_details.png",
    "images/employee_details/Linda Lagos_details.png",
    "images/employee_details/Linnea Bergen_details.png",
    "images/employee_details/Loreto Bodrogi_details.png",
    "images/employee_details/Lucas Alcazar_details.png",
    "images/employee_details/Marin Onda_details.png",
    "images/employee_details/Mat Bramar_details.png",
    "images/employee_details/Minke Mies_details.png",
    "images/employee_details/Nils Calixto_details.png",
    "images/employee_details/Orhan Strum_details.png",
    "images/employee_details/Rachel Pantanal_details.png",
    "images/employee_details/Ruscella Mies Haber_details.png",
    "images/employee_details/Sten Sanjorge Jr._details.png",
    "images/employee_details/Stenig Fusil_details.png",
    "images/employee_details/Sven Flecha_details.png",
    "images/employee_details/Valeria Morlun_details.png",
    "images/employee_details/Varja Lagos_details.png",
    "images/employee_details/Varro Awelon_details.png",
    "images/employee_details/Vira Frente_details.png",
    "images/employee_details/Willem Vasco-Pais_details.png"
];

var employeeSum = [
    "images/employee_summary/Ada Campo-Corrente_summary.png",
    "images/employee_summary/Adan Morlun_summary.png",
    "images/employee_summary/Adra Nubarron_summary.png",
    "images/employee_summary/Albina Hafon_summary.png",
    "images/employee_summary/Anda Ribera_summary.png",
    "images/employee_summary/Axel Calzas_summary.png",
    "images/employee_summary/Benito Hawelon_summary.png",
    "images/employee_summary/Bertrand Ovan_summary.png",
    "images/employee_summary/Birgitta Frente_summary.png",
    "images/employee_summary/Brand Tempestad_summary.png",
    "images/employee_summary/Carla Forluniau_summary.png",
    "images/employee_summary/Cecilia Morluniau_summary.png",
    "images/employee_summary/Claudio Hawelon_summary.png",
    "images/employee_summary/Cornelia Lais_summary.png",
    "images/employee_summary/Dante Coginian_summary.png",
    "images/employee_summary/Dylan Scozzese_summary.png",
    "images/employee_summary/Edvard Vann_summary.png",
    "images/employee_summary/Elsa Orilla_summary.png",
    "images/employee_summary/Emile Arpa_summary.png",
    "images/employee_summary/Felix Balas_summary.png",
    "images/employee_summary/Felix Resumir_summary.png",
    "images/employee_summary/Gustav Cazar_summary.png",
    "images/employee_summary/Henk Mies_summary.png",
    "images/employee_summary/Hennie Osvaldo_summary.png",
    "images/employee_summary/Hideki Cocinaro_summary.png",
    "images/employee_summary/Inga Ferro_summary.png",
    "images/employee_summary/Ingrid Barranco_summary.png",
    "images/employee_summary/Irene Nant_summary.png",
    "images/employee_summary/Isak Baza_summary.png",
    "images/employee_summary/Isande Borrasca_summary.png",
    "images/employee_summary/Isia Vann_summary.png",
    "images/employee_summary/Kanon Herrero_summary.png"];

var locFull = [
    "images/location_full/Abila Airport_full.png",
    "images/location_full/Abila Scrapyard_full.png",
    "images/location_full/Abila Zacharo_full.png",
    "images/location_full/Ahaggo Museum_full.png",
    "images/location_full/Albert's Fine Clothing_full.png",
    "images/location_full/Bean There Done That_full.png",
    "images/location_full/Brew've Been Served_full.png",
    "images/location_full/Brewed Awakenings_full.png",
    "images/location_full/Carlyle Chemical Inc._full.png",
    "images/location_full/Chostus Hotel_full.png",
    "images/location_full/Coffee Cameleon_full.png",
    "images/location_full/Coffee Shack_full.png",
    "images/location_full/Daily Dealz_full.png",
    "images/location_full/Desafio Golf Course_full.png",
    "images/location_full/Frank's Fuel_full.png",
    "images/location_full/Frydos Autosupply n' More_full.png",
    "images/location_full/Gelatogalore_full.png",
    "images/location_full/General Grocer_full.png",
    "images/location_full/Guy's Gyros_full.png",
    "images/location_full/Hallowed Grounds_full.png",
    "images/location_full/Hippokampos_full.png",
    "images/location_full/Jack's Magical Beans_full.png",
    "images/location_full/Kalami Kafenion_full.png",
    "images/location_full/Katerinas Café_full.png",
    "images/location_full/Kronos Mart_full.png",
    "images/location_full/Kronos Pipe and Irrigation_full.png",
    "images/location_full/Maximum Iron and Steel_full.png",
    "images/location_full/Nationwide Refinery_full.png",
    "images/location_full/Octavio's Office Supplies_full.png",
    "images/location_full/Ouzeri Elian_full.png",
    "images/location_full/Roberts and Sons_full.png",
    "images/location_full/Shoppers' Delight_full.png",
    "images/location_full/Stewart and Sons Fabrication_full.png",
    "images/location_full/U-Pump_full.png"];

var locOnly = [
    "images/location_only/Abila Airport_only.png",
    "images/location_only/Abila Scrapyard_only.png",
    "images/location_only/Abila Zacharo_only.png",
    "images/location_only/Ahaggo Museum_only.png",
    "images/location_only/Albert's Fine Clothing_only.png",
    "images/location_only/Bean There Done That_only.png",
    "images/location_only/Brew've Been Served_only.png",
    "images/location_only/Brewed Awakenings_only.png",
    "images/location_only/Carlyle Chemical Inc._only.png",
    "images/location_only/Chostus Hotel_only.png",
    "images/location_only/Coffee Cameleon_only.png",
    "images/location_only/Coffee Shack_only.png",
    "images/location_only/Daily Dealz_only.png",
    "images/location_only/Desafio Golf Course_only.png",
    "images/location_only/Frank's Fuel_only.png",
    "images/location_only/Frydos Autosupply n' More_only.png",
    "images/location_only/Gelatogalore_only.png",
    "images/location_only/General Grocer_only.png",
    "images/location_only/Guy's Gyros_only.png",
    "images/location_only/Hallowed Grounds_only.png",
    "images/location_only/Hippokampos_only.png",
    "images/location_only/Jack's Magical Beans_only.png",
    "images/location_only/Kalami Kafenion_only.png",
    "images/location_only/Katerinas Café_only.png",
    "images/location_only/Kronos Mart_only.png",
    "images/location_only/Kronos Pipe and Irrigation_only.png",
    "images/location_only/Maximum Iron and Steel_only.png",
    "images/location_only/Nationwide Refinery_only.png",
    "images/location_only/Octavio's Office Supplies_only.png",
    "images/location_only/Ouzeri Elian_only.png",
    "images/location_only/Roberts and Sons_only.png",
    "images/location_only/Shoppers' Delight_only.png",
    "images/location_only/Stewart and Sons Fabrication_only.png",
    "images/location_only/U-Pump_only.png"];

$('#graphP').change(function () {
    var val = parseInt($('#graphP').val());
    $('img.detail2').attr("src",employeeSum[val]);
});

$('#graphP').change(function () {
    var val = parseInt($('#graphP').val());
    $('img.detail').attr("src",employeeDetails[val]);
});

$('#graphLoc').change(function () {
    var val = parseInt($('#graphLoc').val());
    $('img.loc').attr("src",locFull[val]);
});

$('#graphLoc').change(function () {
    var val = parseInt($('#graphLoc').val());
    $('img.loc2').attr("src",locOnly[val]);
});

