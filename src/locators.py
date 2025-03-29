"""
This is part of wayrunku-desinformacion-politica
Copyright Rodrigo Garcia 2025
"""

locators = {
    'categorias': {
        'linkPorNombre': {
            'stype': 'xpath',
            # Ejemplos: Bienes Inmuebles, Cultura y Turismo, Impuestos
            'value': lambda nombre: f'//div[@style="text-align: center;"]//div[@class="pb-2 md:pb-5"]/div/span[text()=" {nombre} "]'
        }
    },
    'listaTramites': {
        'linkPorTramite': {
            'stype': 'xpath',
            'value': '//div[@class="pa-5 my-10"]//div[@class="flex-grow"]/div/a/span/..'
        },
        'listPags': {
            'stype': 'css',
            'value': 'div.el-pagination > ul.el-pager li'
        },
        'pagSiguienteBtn': {
            # cuando no hay mas paginas este elemento no existe
            'stype': 'xpath',
            'value': '//button[@class="btn-next"][not(@disabled)]'
        }
        
    },
    'tramites': {
        'titulo': {
            'stype': 'xpath',
            'value': '//div[@class="flex justify-between flex-col sm:flex-row"]/div/span[contains(@class, "uppercase")]'
        },
        'institucion': {
            'stype': 'xpath',
            'value': '//div[@class="flex justify-between flex-col sm:flex-row"]/div/a[@class="text-primary font-semibold"]'
        
        },
        'descripcion': {
            'stype': 'xpath',
            'value': '//div[@class="py-5 text-justify animate-paragraph"]'
        },
        'contacto': {
            'stype': 'xpath',
            #'value': '//div[@class="flex justify-between flex-col sm:flex-row"]//div[1]/a'
            'value': '//div[@class="flex justify-between flex-col sm:flex-row"]//div/a[contains(@href, "mailto:")]'
        },
        'web': {
            'stype': 'xpath',
            'value': '//div[@class="flex justify-between flex-col sm:flex-row"]//div[2]/a'
        },
        'tipoTramite1': {
            'stype': 'xpath',
            'value': '//div[@id="tab-0"]/span[contains(@class, "sm:text-base")]'
        },
        'tipoTramite2': {
            'stype': 'xpath',
            'value': '//div[@id="tab-1"]/span[contains(@class, "sm:text-base")]'

        },
        'botonIniciarTramiteEnLinea': {
            'stype': 'xpath',
            'value': '//span[@class="text-base sm:text-lg"][text()="Iniciar trámite en línea"]'
        },
        'queNecesitoText': {
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()="¿Qué necesito?"]/../div',
        },
        'comoYDondeTexto': {
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()="¿Cómo y dónde hago el trámite?"]/../div'
        },
        'direccionesTramite': {
            # pueden haber multiples elementos
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()="Direcciones donde se realiza este trámite"]/../div//div[@role="tablist"]//div[@class="el-collapse-item__content"]/div'
        },
        'masInfo': {
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()="Más información"]/../div'
        },
        'ultimaActualizacion': {
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()="Más información"]/..//div/span[contains(text(),"Última  actualización de la Información:")]/..'
        },
        'observaciones': {
            # podria no existir
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()="Más información"]/..//div/span[contains(text(),"Observaciones:")]/..'
        },
        'costoTexto': {
            # podria no existir
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()=" Costo del Trámite"]/../div'
        },
        'costoMontos': {
            # podria no existir
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()=" Costo del Trámite"]/../div//span[text()="Monto:"]/..'
        },
        'costoFormas': {
            # podria no existir
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()=" Costo del Trámite"]/../div//span[text()="Forma de pago:"]/..'
        },
        'costoConceptos': {
            # podria no existir
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()=" Costo del Trámite"]/../div//span[text()="Concepto de pago:"]/..'
        },
        'costoCtasBancarias': {
            'stype': 'xpath',
            'value': '//div[@class="animate-paragraph"]/h2[text()=" Costo del Trámite"]/../div//span[contains(text(),"N° Cuenta Bancaria")]/..'
        },
        'rateYellow': {
            # podria no existir
            'stype': 'xpath',
            'value': '//div[@class="flex justify-between flex-col sm:flex-row"]//span[@class="el-rate__item"]/i[@style="color:#F3C800;"]'
        },
        'rateRed': {
            # podria no existir
            'stype': 'xpath',
            'value': '//div[@class="flex justify-between flex-col sm:flex-row"]//span[@class="el-rate__item"]/i[@style="color:#FA0D00;"]'
        },
        'rateGreen': {
            # podria no existir
            'stype': 'xpath',
            'value': '//div[@class="flex justify-between flex-col sm:flex-row"]//span[@class="el-rate__item"]/i[@style="color:#5DD90F;"]'
        }
    }
}


