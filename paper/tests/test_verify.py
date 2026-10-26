import copy, hashlib, json, tempfile, unittest
from pathlib import Path
import verify

class VerificationTests(unittest.TestCase):
 def setUp(self):
  self.c=[{'report_id':'11111111-1111-1111-1111-111111111111','program_sha256':'a'*64,'file_sha256':'b'*64}]
  self.e=[{'event_id':'one','report_id':self.c[0]['report_id'],'method':'POST','status':'200'}]
 def test_complete_2xx_range(self):
  for status in range(100,600):
   with self.subTest(status=status):self.assertEqual(verify.is_2xx(str(status)),200<=status<=299)
 def test_invalid_statuses(self):
  for status in ['',None,True,False,200.0,'200 OK','0200','200\n',{},[]]:
   with self.subTest(status=repr(status)):self.assertFalse(verify.is_2xx(status))
 def test_options_does_not_count(self):
  self.e[0]['method']='OPTIONS'; self.assertEqual(verify.summarize(self.c,self.e,[])['post_2xx'],0)
 def test_missing_not_failure(self):
  self.e[0]['status']=None; out=verify.summarize(self.c,self.e,[]);self.assertEqual((out['post_missing_status'],out['post_2xx']),(1,0))
 def test_duplicate_id_rejected(self):
  with self.assertRaises(ValueError):verify.summarize(self.c*2,self.e,[])
 def test_orphan_rejected(self):
  self.e[0]['report_id']='missing'
  with self.assertRaises(ValueError):verify.summarize(self.c,self.e,[])
 def test_duplicate_event_rejected(self):
  with self.assertRaises(ValueError):verify.summarize(self.c,self.e*2,[])
 def test_group_unit(self):
  second=copy.deepcopy(self.c[0]);second['report_id']='22222222-2222-2222-2222-222222222222'
  second_e=copy.deepcopy(self.e[0]);second_e.update(event_id='two',report_id=second['report_id'])
  out=verify.summarize(self.c+[second],self.e+[second_e],[])
  self.assertEqual((out['post_2xx_reports'],out['post_2xx_programs']),(2,1))
 def test_integrity_and_rejection(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);(root/'good.txt').write_bytes(b'held bytes')
   (root/'MANIFEST.json').write_text(json.dumps({'good.txt':hashlib.sha256(b'held bytes').hexdigest()}),encoding='utf-8')
   self.assertEqual(verify.verify_inventory(root),1)
   (root/'good.txt').write_bytes(b'changed bytes')
   with self.assertRaises(ValueError):verify.verify_inventory(root)
 def test_extra_member_rejected(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);(root/'MANIFEST.json').write_text('{}',encoding='utf-8');(root/'extra.txt').write_bytes(b'harmless')
   with self.assertRaises(ValueError):verify.verify_inventory(root)
if __name__=='__main__':unittest.main()
