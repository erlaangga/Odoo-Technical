from openerp.osv import osv,fields

class Pelajaran(osv.osv):
    _name = "data.pelajaran"
    
    _columns = {
                "name":fields.char("Nama"),
                "id_pelajaran":fields.char("ID Pelajaran",size=10),
                "state":fields.selection([("draft","Draft"),("penunjang","Penunjang"), ("wajib","Wajib")], string="State")
                }
    
    _defaults = {
                 "state": "draft",
                 "id_pelajaran":1234
                 }