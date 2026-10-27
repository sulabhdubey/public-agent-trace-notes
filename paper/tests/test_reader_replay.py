import copy
import unittest
import verify

class ReaderReplayTests(unittest.TestCase):
 def setUp(self):
  self.a='11111111-1111-1111-1111-111111111111';self.b='22222222-2222-2222-2222-222222222222'
  self.c=[{'report_id':self.a,'program_sha256':'a'*64,'file_sha256':'b'*64}]
  self.s=[{'report_id':self.a,'acquisition_status':'acquired'},{'report_id':self.b,'acquisition_status':'not_acquired'}]
  self.e=[{'event_id':'one','report_id':self.a,'method':'POST','status':'206'}]
 def test_selection_partition_and_exact_missing_id(self):
  self.assertEqual(verify.selection_summary(self.s,self.c),{'selected':2,'acquired':1,'not_acquired':1,'not_acquired_report_ids':[self.b]})
 def test_missing_acquired_id_rejected(self):
  with self.assertRaisesRegex(ValueError,'disagree'):verify.selection_summary(self.s[1:],self.c)
 def test_unheld_report_marked_acquired_rejected(self):
  self.s[1]['acquisition_status']='acquired'
  with self.assertRaisesRegex(ValueError,'disagree'):verify.selection_summary(self.s,self.c)
 def test_acquired_report_marked_absent_rejected(self):
  self.s[0]['acquisition_status']='not_acquired'
  with self.assertRaisesRegex(ValueError,'disagree'):verify.selection_summary(self.s,self.c)
 def test_duplicate_selection_rejected(self):
  with self.assertRaisesRegex(ValueError,'Duplicate'):verify.selection_summary(self.s+self.s[:1],self.c)
 def test_unknown_acquisition_status_rejected(self):
  self.s[1]['acquisition_status']='failed'
  with self.assertRaisesRegex(ValueError,'status'):verify.selection_summary(self.s,self.c)
 def test_extra_selection_columns_rejected(self):
  self.s[0]['payload']='not an allowed column'
  with self.assertRaisesRegex(ValueError,'columns'):verify.selection_summary(self.s,self.c)
 def test_table_uses_actual_changed_status_and_year(self):
  out=verify.headline_tables(self.c,self.e,[{'date':'2021-01-01'}],self.s)
  self.assertEqual(out['post_statuses'],{'206':1});self.assertEqual(out['catalog_years'],{'2021':1})
  text=verify.markdown_tables(out);self.assertIn('| 206 | 1 |',text);self.assertIn('| 2021 | 1 |',text)
 def test_integer_and_string_statuses_join(self):
  e=copy.deepcopy(self.e[0]);e.update(event_id='two',status=206)
  out=verify.headline_tables(self.c,self.e+[e],[],self.s)
  self.assertEqual(out['post_statuses'],{'206':2})
 def test_missing_status_stays_separate_from_error(self):
  self.e[0]['status']=None
  e=copy.deepcopy(self.e[0]);e.update(event_id='two',status='400')
  self.assertEqual(verify.headline_tables(self.c,self.e+[e],[],self.s)['post_statuses'],{'400':1,'Missing':1})
 def test_invalid_status_not_silently_counted(self):
  for bad in (True,200.0,'200 OK','0200','999',[],{}):
   with self.subTest(bad=repr(bad)):
    self.e[0]['status']=bad
    with self.assertRaises(ValueError):verify.summarize(self.c,self.e,[])
 def test_options_not_in_post_table(self):
  self.e[0]['method']='OPTIONS'
  self.assertEqual(verify.headline_tables(self.c,self.e,[],self.s)['post_statuses'],{})

if __name__=='__main__':unittest.main()
