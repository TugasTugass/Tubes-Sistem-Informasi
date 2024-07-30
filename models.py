from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Pembeli(db.Model):
    __tablename__ = 'pembeli'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    kata_sandi = db.Column(db.String(255), nullable=False)
    telepon = db.Column(db.String(15))

    pesanan = db.relationship("Pesanan", back_populates="pembeli")
    alamat = db.relationship("Alamat", back_populates="pembeli")

class Pesanan(db.Model):
    __tablename__ = 'pesanan'
    id = db.Column(db.Integer, primary_key=True)
    id_pembeli = db.Column(db.Integer, db.ForeignKey('pembeli.id'), nullable=False)
    tanggal_pesanan = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False)
    total_harga = db.Column(db.DECIMAL(10, 2), nullable=False)

    pembeli = db.relationship("Pembeli", back_populates="pesanan")
    pembayaran = db.relationship("Pembayaran", back_populates="pesanan")
    produk = db.relationship("Produk", secondary="pesanan_produk", back_populates="pesanan")

class Produk(db.Model):
    __tablename__ = 'produk'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    harga = db.Column(db.DECIMAL(10, 2), nullable=False)
    stok = db.Column(db.Integer, nullable=False)
    id_kategori = db.Column(db.Integer, nullable=False)

    pesanan = db.relationship("Pesanan", secondary="pesanan_produk", back_populates="produk")

class Pembayaran(db.Model):
    __tablename__ = 'pembayaran'
    id = db.Column(db.Integer, primary_key=True)
    id_pesanan = db.Column(db.Integer, db.ForeignKey('pesanan.id'), nullable=False)
    metode_pembayaran = db.Column(db.String(50), nullable=False)
    tanggal_pembayaran = db.Column(db.DateTime, default=datetime.utcnow)
    jumlah = db.Column(db.DECIMAL(10, 2), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    pesanan = db.relationship("Pesanan", back_populates="pembayaran")

class Alamat(db.Model):
    __tablename__ = 'alamat'
    id = db.Column(db.Integer, primary_key=True)
    id_pembeli = db.Column(db.Integer, db.ForeignKey('pembeli.id'), nullable=False)
    jalan = db.Column(db.String(255), nullable=False)
    kota = db.Column(db.String(100), nullable=False)
    provinsi = db.Column(db.String(100), nullable=False)
    kode_pos = db.Column(db.String(10), nullable=False)
    negara = db.Column(db.String(100), nullable=False)

    pembeli = db.relationship("Pembeli", back_populates="alamat")

pesanan_produk = db.Table('pesanan_produk',
    db.Column('id_pesanan', db.Integer, db.ForeignKey('pesanan.id'), primary_key=True),
    db.Column('id_produk', db.Integer, db.ForeignKey('produk.id'), primary_key=True)
)