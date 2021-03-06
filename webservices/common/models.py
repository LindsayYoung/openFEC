from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


class Candidate(db.Model):
    candidate_key = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.String(10))
    candidate_status = db.Column(db.String(1))
    candidate_status_full = db.Column(db.String(11))
    district = db.Column(db.String(2))
    active_through = db.Column(db.Integer)
    election_years = db.Column(ARRAY(db.Integer))
    incumbent_challenge = db.Column(db.String(1))
    incumbent_challenge_full = db.Column(db.String(10))
    office = db.Column(db.String(1))
    office_full = db.Column(db.String(9))
    party = db.Column(db.String(3))
    party_full = db.Column(db.String(255))
    state = db.Column(db.String(2))
    name = db.Column(db.String(100))
    committees = db.relationship('CandidateCommitteeLink', backref='candidates')

    __tablename__ = 'ofec_candidates_vw'

class CandidateDetail(db.Model):
    candidate_key = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.String(10))
    candidate_status = db.Column(db.String(1))
    candidate_status_full = db.Column(db.String(11))
    district = db.Column(db.String(2))
    active_through = db.Column(db.Integer)
    election_years = db.Column(ARRAY(db.Integer))
    incumbent_challenge = db.Column(db.String(1))
    incumbent_challenge_full = db.Column(db.String(10))
    office = db.Column(db.String(1))
    office_full = db.Column(db.String(9))
    party = db.Column(db.String(3))
    party_full = db.Column(db.String(255))
    state = db.Column(db.String(2))
    name = db.Column(db.String(100))
    expire_date = db.Column('candidate_expire_date', db.DateTime())
    load_date = db.Column(db.DateTime())
    form_type = db.Column(db.String(3))
    address_city = db.Column(db.String(100))
    address_state = db.Column(db.String(2))
    address_street_1 = db.Column(db.String(200))
    address_street_2 = db.Column(db.String(200))
    address_zip = db.Column(db.String(10))
    candidate_inactive = db.Column(db.String(1))
    committees = db.relationship('CandidateCommitteeLink', backref='candidatedetail')

    __tablename__ = 'ofec_candidate_detail_vw'


class Committee(db.Model):
    committee_key = db.Column(db.Integer, primary_key=True)
    committee_id = db.Column(db.String(9))
    designation = db.Column(db.String(1))
    designation_full = db.Column(db.String(25))
    treasurer_name = db.Column(db.String(100))
    organization_type = db.Column(db.String(1))
    organization_type_full = db.Column(db.String(100))
    state = db.Column(db.String(2))
    committee_type = db.Column(db.String(1))
    committee_type_full = db.Column(db.String(50))
    expire_date = db.Column(db.DateTime())
    party = db.Column(db.String(3))
    party_full = db.Column(db.String(50))
    original_registration_date = db.Column(db.DateTime())
    name = db.Column(db.String(100))
    candidates = db.relationship('CandidateCommitteeLink', backref='committees')


    __tablename__ = 'ofec_committees_vw'


class CommitteeDetail(db.Model):
    committee_key = db.Column(db.Integer, primary_key=True)
    committee_id = db.Column(db.String(9))
    designation = db.Column(db.String(1))
    designation_full = db.Column(db.String(25))
    treasurer_name = db.Column(db.String(100))
    organization_type = db.Column(db.String(1))
    organization_type_full = db.Column(db.String(100))
    state = db.Column(db.String(2))
    committee_type = db.Column(db.String(1))
    committee_type_full = db.Column(db.String(50))
    expire_date = db.Column(db.DateTime())
    party = db.Column(db.String(3))
    party_full = db.Column(db.String(50))
    original_registration_date = db.Column(db.DateTime())
    name = db.Column(db.String(100))
    candidates = db.relationship('CandidateCommitteeLink', backref='committeedetail')
    # detail view additions
    filing_frequency = db.Column(db.String(1))
    email = db.Column(db.String(50))
    fax = db.Column(db.String(10))
    website = db.Column(db.String(50))
    form_type = db.Column(db.String(3))
    leadership_pac = db.Column(db.String(50))
    load_date = db.Column(db.DateTime())
    lobbyist_registrant_pac = db.Column(db.String(1))
    party_type = db.Column(db.String(3))
    party_type_full = db.Column(db.String(15))
    qualifying_date = db.Column(db.DateTime())
    street_1 = db.Column(db.String(50))
    street_2 = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state_full = db.Column(db.String(50))
    zip = db.Column(db.String(9))
    treasurer_city = db.Column(db.String(50))
    treasurer_name_1 = db.Column(db.String(50))
    treasurer_name_2 = db.Column(db.String(50))
    treasurer_name_middle = db.Column(db.String(50))
    treasurer_name_prefix = db.Column(db.String(50))
    treasurer_phone = db.Column(db.String(15))
    treasurer_state = db.Column(db.String(50))
    treasurer_street_1 = db.Column(db.String(50))
    treasurer_street_2 = db.Column(db.String(50))
    treasurer_name_suffix = db.Column(db.String(50))
    treasurer_name_title = db.Column(db.String(50))
    treasurer_zip = db.Column(db.String(9))
    custodian_city = db.Column(db.String(50))
    custodian_name_1 = db.Column(db.String(50))
    custodian_name_2 = db.Column(db.String(50))
    custodian_name_middle = db.Column(db.String(50))
    custodian_name_full = db.Column(db.String(100))
    custodian_phone = db.Column(db.String(15))
    custodian_name_prefix = db.Column(db.String(50))
    custodian_state = db.Column(db.String(2))
    custodian_street_1 = db.Column(db.String(50))
    custodian_street_2 = db.Column(db.String(50))
    custodian_name_suffix = db.Column(db.String(50))
    custodian_name_title = db.Column(db.String(50))
    custodian_zip = db.Column(db.String(9))

    __tablename__ = 'ofec_committee_detail_vw'


class CandidateCommitteeLink(db.Model):
    linkage_key = db.Column(db.Integer, primary_key=True)
    committee_key = db.Column('committee_key', db.Integer, db.ForeignKey(Committee.committee_key), db.ForeignKey(CommitteeDetail.committee_key))
    candidate_key = db.Column('candidate_key', db.Integer, db.ForeignKey(Candidate.candidate_key), db.ForeignKey(CandidateDetail.candidate_key))
    committee_id = db.Column('committee_id', db.String(10))
    candidate_id = db.Column('candidate_id', db.String(10))
    election_year = db.Column('election_year', db.Integer)
    active_through = db.Column('active_through', db.Integer)
    link_date = db.Column('link_date', db.DateTime())
    expire_date = db.Column('expire_date', db.DateTime())
    committee_name = db.Column('committee_name', db.DateTime())
    candidate_name = db.Column('candidate_name', db.DateTime())
    committee_designation = db.Column('committee_designation', db.String(1))
    committee_designation_full = db.Column(db.String(25))
    committee_type = db.Column('committee_type', db.String(1))
    committee_type_full = db.Column('committee_type_full', db.String(50))

    __tablename__ = 'ofec_name_linkage_vw'



