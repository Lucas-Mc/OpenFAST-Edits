import unittest
import os
from src.base_case import BaseCase
from src.beamdyn_driver import BeamdynDriver
from src.beamdyn_files import BeamdynDriverFile


class TestBaseCase(unittest.TestCase):

  def test_start(self):

    baseline_cd = os.path.dirname(os.path.realpath(__file__))
    baseline_driver_path = os.path.join(baseline_cd,'beamdyn_driver')
    baseline_driver = BeamdynDriver(baseline_driver_path)
    baseline_if = [BeamdynDriverFile(baseline_cd, 'bd_driver.yml')]
    baseline_case = BaseCase(baseline_driver,baseline_cd,baseline_if)
    
    new_dir = os.path.abspath(os.path.join(baseline_cd, os.pardir))
    # os.chdir(baseline_cd.replace('/tests',''))
    os.chdir(new_dir)
    cd_before = os.getcwd()
    BaseCase.end(baseline_case)
    cd_after = os.getcwd()
    self.assertNotEqual(cd_before,cd_after)

    self.assertEqual(cd_after,baseline_cd)

  def test_run(self):

    baseline_cd = os.path.dirname(os.path.realpath(__file__))
    baseline_driver_path = os.path.join(baseline_cd,'beamdyn_driver')
    baseline_driver = BeamdynDriver(baseline_driver_path)
    baseline_if = [BeamdynDriverFile(baseline_cd, 'bd_driver.yml')]
    baseline_case = BaseCase(baseline_driver,baseline_cd,baseline_if)
    
    test_output = BaseCase.run(baseline_case)

    self.assertEqual(test_output,0)

  def test_end(self):

    baseline_cd = os.path.dirname(os.path.realpath(__file__))
    baseline_driver_path = os.path.join(baseline_cd,'beamdyn_driver')
    baseline_driver = BeamdynDriver(baseline_driver_path)
    baseline_if = [BeamdynDriverFile(baseline_cd, 'bd_driver.yml')]
    baseline_case = BaseCase(baseline_driver,baseline_cd,baseline_if)
    
    new_dir = os.path.abspath(os.path.join(baseline_cd, os.pardir))
    # os.chdir(baseline_cd.replace('/tests',''))
    os.chdir(new_dir)
    cd_before = os.getcwd()
    BaseCase.end(baseline_case)
    cd_after = os.getcwd()

    self.assertNotEqual(cd_before,cd_after)
    self.assertEqual(cd_after,baseline_cd)

def tearDownModule():
    # Clean up and remove all temporary files
    os.remove('bd_primary.inp.ech')
    os.remove('bd_primary.inp.sum')
    os.remove('tests.log')


if __name__ == '__main__':
  unittest.main()