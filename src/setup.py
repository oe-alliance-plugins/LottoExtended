from setuptools import setup
import setup_translate

pkg = 'Extensions.LottoExtended'
setup(name='enigma2-plugin-extensions-lottoextended',
       version='3.0',
       description='Eigene Lottotipps bequem auf dem TV abrufen und auswerten',
       package_dir={pkg: 'LottoExtended'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
