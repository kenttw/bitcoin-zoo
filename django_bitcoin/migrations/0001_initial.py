# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transaction'
        db.create_table(u'django_bitcoin_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=16, decimal_places=8)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'django_bitcoin', ['Transaction'])

        # Adding model 'DepositTransaction'
        db.create_table(u'django_bitcoin_deposittransaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_bitcoin.BitcoinAddress'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=16, decimal_places=8)),
            ('description', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
            ('wallet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_bitcoin.Wallet'])),
            ('under_execution', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['django_bitcoin.WalletTransaction'], null=True)),
            ('confirmations', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('txid', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'django_bitcoin', ['DepositTransaction'])

        # Adding model 'OutgoingTransaction'
        db.create_table(u'django_bitcoin_outgoingtransaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('expires_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('executed_at', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True)),
            ('under_execution', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('to_bitcoinaddress', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=16, decimal_places=8)),
            ('txid', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'django_bitcoin', ['OutgoingTransaction'])

        # Adding model 'BitcoinAddress'
        db.create_table(u'django_bitcoin_bitcoinaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('pkey1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pkey2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pkey3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pkey4', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('least_received', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=16, decimal_places=8)),
            ('least_received_confirmed', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=16, decimal_places=8)),
            ('label', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('wallet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='addresses', null=True, to=orm['django_bitcoin.Wallet'])),
            ('migrated_to_transactions', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'django_bitcoin', ['BitcoinAddress'])

        # Adding model 'Payment'
        db.create_table(u'django_bitcoin_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=16, decimal_places=8)),
            ('amount_paid', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=16, decimal_places=8)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('paid_at', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True)),
            ('withdrawn_total', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=16, decimal_places=8)),
        ))
        db.send_create_signal(u'django_bitcoin', ['Payment'])

        # Adding M2M table for field transactions on 'Payment'
        m2m_table_name = db.shorten_name(u'django_bitcoin_payment_transactions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('payment', models.ForeignKey(orm[u'django_bitcoin.payment'], null=False)),
            ('transaction', models.ForeignKey(orm[u'django_bitcoin.transaction'], null=False))
        ))
        db.create_unique(m2m_table_name, ['payment_id', 'transaction_id'])

        # Adding model 'WalletTransaction'
        db.create_table(u'django_bitcoin_wallettransaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('from_wallet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sent_transactions', null=True, to=orm['django_bitcoin.Wallet'])),
            ('to_wallet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='received_transactions', null=True, to=orm['django_bitcoin.Wallet'])),
            ('to_bitcoinaddress', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('outgoing_transaction', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['django_bitcoin.OutgoingTransaction'], null=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=16, decimal_places=8)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('deposit_address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_bitcoin.BitcoinAddress'], null=True)),
            ('txid', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('deposit_transaction', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['django_bitcoin.DepositTransaction'], unique=True, null=True)),
        ))
        db.send_create_signal(u'django_bitcoin', ['WalletTransaction'])

        # Adding model 'Wallet'
        db.create_table(u'django_bitcoin_wallet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('transaction_counter', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('last_balance', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=16, decimal_places=8)),
        ))
        db.send_create_signal(u'django_bitcoin', ['Wallet'])

        # Adding model 'HistoricalPrice'
        db.create_table(u'django_bitcoin_historicalprice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('params', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'django_bitcoin', ['HistoricalPrice'])


    def backwards(self, orm):
        # Deleting model 'Transaction'
        db.delete_table(u'django_bitcoin_transaction')

        # Deleting model 'DepositTransaction'
        db.delete_table(u'django_bitcoin_deposittransaction')

        # Deleting model 'OutgoingTransaction'
        db.delete_table(u'django_bitcoin_outgoingtransaction')

        # Deleting model 'BitcoinAddress'
        db.delete_table(u'django_bitcoin_bitcoinaddress')

        # Deleting model 'Payment'
        db.delete_table(u'django_bitcoin_payment')

        # Removing M2M table for field transactions on 'Payment'
        db.delete_table(db.shorten_name(u'django_bitcoin_payment_transactions'))

        # Deleting model 'WalletTransaction'
        db.delete_table(u'django_bitcoin_wallettransaction')

        # Deleting model 'Wallet'
        db.delete_table(u'django_bitcoin_wallet')

        # Deleting model 'HistoricalPrice'
        db.delete_table(u'django_bitcoin_historicalprice')


    models = {
        u'django_bitcoin.bitcoinaddress': {
            'Meta': {'object_name': 'BitcoinAddress'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'least_received': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '8'}),
            'least_received_confirmed': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '8'}),
            'migrated_to_transactions': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pkey1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pkey2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pkey3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pkey4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'user': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'wallet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addresses'", 'null': 'True', 'to': u"orm['django_bitcoin.Wallet']"})
        },
        u'django_bitcoin.deposittransaction': {
            'Meta': {'object_name': 'DepositTransaction'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_bitcoin.BitcoinAddress']"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '8'}),
            'confirmations': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['django_bitcoin.WalletTransaction']", 'null': 'True'}),
            'txid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'under_execution': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wallet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_bitcoin.Wallet']"})
        },
        u'django_bitcoin.historicalprice': {
            'Meta': {'object_name': 'HistoricalPrice'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'params': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'})
        },
        u'django_bitcoin.outgoingtransaction': {
            'Meta': {'object_name': 'OutgoingTransaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'executed_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'expires_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_bitcoinaddress': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'txid': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'under_execution': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'django_bitcoin.payment': {
            'Meta': {'object_name': 'Payment'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'}),
            'amount_paid': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'transactions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['django_bitcoin.Transaction']", 'symmetrical': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {}),
            'withdrawn_total': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'})
        },
        u'django_bitcoin.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'django_bitcoin.wallet': {
            'Meta': {'object_name': 'Wallet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'last_balance': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '8'}),
            'transaction_counter': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'transactions_with': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['django_bitcoin.Wallet']", 'through': u"orm['django_bitcoin.WalletTransaction']", 'symmetrical': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'django_bitcoin.wallettransaction': {
            'Meta': {'object_name': 'WalletTransaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '16', 'decimal_places': '8'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'deposit_address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_bitcoin.BitcoinAddress']", 'null': 'True'}),
            'deposit_transaction': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['django_bitcoin.DepositTransaction']", 'unique': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'from_wallet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_transactions'", 'null': 'True', 'to': u"orm['django_bitcoin.Wallet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outgoing_transaction': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['django_bitcoin.OutgoingTransaction']", 'null': 'True'}),
            'to_bitcoinaddress': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'to_wallet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'received_transactions'", 'null': 'True', 'to': u"orm['django_bitcoin.Wallet']"}),
            'txid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['django_bitcoin']