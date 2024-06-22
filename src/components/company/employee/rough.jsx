import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import FinBase from './FinBase'; // Assuming FinBase is another component

const EmployeeForm = () => {
  const [formData, setFormData] = useState({
    Title: '',
    First_Name: '',
    Last_Name: '',
    Alias: '',
    Joining_Date: '',
    Salary_Date: '',
    Salary_Type: '',
    Salary_Amount: '',
    Amount_Per_Hour: '',
    Total_Working_Hours: '',
    Employee_Number: '',
    Designation: '',
    Location: '',
    Gender: '',
    DOB: '',
    Blood: '',
    Contact_Number: '',
    Emergency_Contact_Number: '',
    Personal_Email: '',
    Parent: '',
    Spouse: '',
    file: null,
    Bank_Details: '',
    TDS_Applicable: '',
    Account_Number: '',
    IFSC: '',
    BankName: '',
    BranchName: '',
    Transaction_Type: '',
    TDS_Type: '',
    TDS_Amount: '',
    Income_Tax: '',
    Aadhar: '',
    UAN: '',
    PF: '',
    PAN: '',
    PR: '',
    Present_Address: {
      address: '',
      city: '',
      state: '',
      pincode: '',
    },
    Permanent_Address: {
      address: '',
      city: '',
      state: '',
      pincode: '',
    },
  });

  const [sameAddress, setSameAddress] = useState(false);
  const [isBankInfoVisible, setIsBankInfoVisible] = useState(false);
  const [isTdsInfoVisible, setIsTdsInfoVisible] = useState(false);
  const [isTdsPercentageVisible, setIsTdsPercentageVisible] = useState(false);
  const [isTdsAmountVisible, setIsTdsAmountVisible] = useState(false);
  const [newUnit, setNewUnit] = useState('');
  const handleSubmit = (e) => {
    e.preventDefault();

    var dt = {
      Id: ID,
      upload_file:'',
      upload_image:'',
      title:Title,
      first_name:First_Name,
      last_name:Last_Name,
      alias:Alias,
      employee_mail:Email,
      employee_number:Employee_Number,
      employee_designation:Designation,
      function:'',
      employee_current_location:CurrentLocation,
      mobile:contact,
      date_of_joining:joiningDate,
      employee_salary_type:salaryType,
      salary_details:salary_details,
      salary_effective_from:Salary_Date,

      pay_head:'',
      salary_amount:salaryAmount,
      amount_per_hour:amountPerHour,
      total_working_hours:workingHours,
      gender:Gender,
      date_of_birth:DOB,
      age:age,
      blood_group:Blood,
      fathers_name_mothers_name:parent,
      spouse_name:Spouse,
      emergency_contact:Number2,
      provide_bank_details:bankDetails,
      account_number:Account_Number,
      ifsc:IFSC,
      name_of_bank:BankName,
      branch_name:branch_name,
      bank_transaction_type:transactionType,
      tds_applicable:tdsApplicable,
      tds_type:tdsType,
      percentage_amount:TDS_Amount,
      pan_number:PAN,
      income_tax_number:Income_Tax,
      aadhar_number:Aadhar,
      universal_account_number:UAN,
      pf_account_number:PF,
      pr_account_number:PR,
      esi_number:esi_number,

      street:presentAddress.address,
      city:presentAddress.city,
      state:presentAddress.state,
      pincode:presentAddress.pincode,
      country:'',
      temporary_street:permanentAddress.address,
      temporary_city:permanentAddress.city,
      temporary_state:permanentAddress.state,
      temporary_pincode:permanentAddress.pincode,
      temporary_country :'',
      employee_status: "Active",
      
     
    };

    axios
      .post(`${config.base_url}/employee_save/`, dt)
      .then((res) => {
        console.log("ITM RES=", res);
        if (res.data.status) {
          Toast.fire({
            icon: "success",
            title: "Item Created",
          });
          navigate("/items");
        }
        if (!res.data.status && res.data.message != "") {
          Swal.fire({
            icon: "error",
            title: `${res.data.message}`,
          });
        }
      })
      .catch((err) => {
        console.log("ERROR=", err);
        if (!err.response.data.status) {
          Swal.fire({
            icon: "error",
            title: `${err.response.data.message}`,
          });
        }
      });
  };

// Continued from the previous code snippet...
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleAddressChange = (type, e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [type]: {
        ...prevData[type],
        [name]: value,
      },
    }));
  };

  const handleFileChange = (e) => {
    setFormData((prevData) => ({
      ...prevData,
      file: e.target.files[0],
    }));
  };

  const handleSameAddressChange = () => {
    setSameAddress(!sameAddress);
    if (!sameAddress) {
      setFormData((prevData) => ({
        ...prevData,
        Permanent_Address: { ...prevData.Present_Address },
      }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission
  };

  const handleSalaryTypeChange = (e) => {
    const { value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      Salary_Type: value,
    }));
  };

  const handleUnitModalSubmit = (e) => {
    e.preventDefault();
    // Add new unit logic
  };

  return (
    <>
      <FinBase />
      <div className="page-content mt-0 pt-0" style={{ backgroundColor: "#2f516f", minHeight: "100vh" }}>
        <div className="d-flex justify-content-end mb-1">
          <Link to={"/items"}>
            <i className="fa fa-times-circle text-white mx-4 p-1" style={{ fontSize: "1.2rem", marginRight: "0rem !important" }}></i>
          </Link>
        </div>
        <div className="card radius-15 h-20">
          <div className="row">
            <div className="col-md-12">
              <center>
                <h2 className="mt-3">CREATE EMPLOYEE</h2>
              </center>
              <hr />
            </div>
          </div>
        </div>
        <div className="card radius-15">
          <div className="card-body">
            <form onSubmit={handleSubmit} className="needs-validation px-1" validate>
              <br />
              <div className="row w-100">
                <div className="col-md-12 mx-0">
                  <div className="row">
                    <div className="col-md-6">
                      <div className="form-group">
                        <label>Title</label>
                        <select id="Title" name="Title" className="form-control" onChange={handleChange} value={formData.Title}>
                          <option value="">Choose...</option>
                          <option value="Mr">Mr</option>
                          <option value="Ms">Ms</option>
                          <option value="Mrs">Mrs</option>
                        </select>
                      </div>
                      <div className="form-group">
                        <label>First Name</label>
                        <input placeholder="First Name" type="text" id="First_Name" name="First_Name" className="form-control" onChange={handleChange} value={formData.First_Name} />
                      </div>
                      <div className="form-group">
                        <label>Last Name</label>
                        <input placeholder="Last Name" type="text" id="Last_Name" name="Last_Name" className="form-control" onChange={handleChange} value={formData.Last_Name} />
                      </div>
                    </div>
                    <div className="col-md-6 d-flex flex-column align-items-center">
                      <label htmlFor="Image" className="mt-5 ml-5 mt-5" style={{
                        cursor: 'pointer',
                        padding: '20% 35%',
                        backgroundImage: "url('static/assets/images/upload.png')",
                        backgroundRepeat: 'no-repeat',
                        backgroundSize: 'contain',
                      }}></label>
                      <span>Upload Image</span>
                      <input type="file" name="Image" id="Image" accept="image/*" style={{ display: 'none' }} onChange={handleFileChange} />
                    </div>
                  </div>
                  <br />
                  <div className="row">
                    <div className="col">
                      <div className="form-group">
                        <label>Alias (optional)</label>
                        <input placeholder="Alias" type="text" id="Alias" name="Alias" className="form-control" onChange={handleChange} value={formData.Alias} />
                      </div>
                      <div className="form-group">
                        <label>Date of Joining</label>
                        <input placeholder="Joining Date" required type="date" id="Joining_Date" name="Joining_Date" className="form-control" onChange={handleChange} value={formData.Joining_Date} />
                      </div>
                    </div>
                    <div className="col">
                      <div className="form-group">
                        <label>Salary Date</label>
                        <select type="date" id="Salary_Date" name="Salary_Date" className="form-control" onChange={handleChange} value={formData.Salary_Date}>
                          <option value="">--select--</option>
                          <option value="1-10">1-10</option>
                          <option value="11-15">11-15</option>
                          <option value="16-31">16-31</option>
                        </select>
                      </div>
                      <div className="form-group">
                        <label>Define salary details</label>
                        <select id="Salary_Type" name="Salary_Type" className="form-control" onChange={handleSalaryTypeChange} value={formData.Salary_Type}>
                          <option value="">--select--</option>
                          <option value="Fixed">Fixed</option>
                          <option value="Temporary">Temporary</option>
                          <option value="Time Based">Time Based</option>
                        </select>
                        {(formData.Salary_Type === 'Fixed' || formData.Salary_Type === 'Temporary' || formData.Salary_Type === 'Time Based') && (
                          <div className="form-group" id="salary_amount">
                            <label>Salary Amount</label>
                            <input placeholder="Salary Amount" name="Salary_Amount" id="salary_amount2" type="text" className="form-control" value={formData.Salary_Amount} onChange={handleChange} readOnly={formData.Salary_Type === 'Time Based'} />
                          </div>
                        )}
                        {formData.Salary_Type === 'Time Based' && (
                          <>
                            <div className="form-group" id="amount_per_hour">
                              <label>Amount Per Hour</label>
                              <input placeholder="Amount Per Hour" name="Amount_Per_Hour" id="amount_per_hour2" type="text" className="form-control" value={formData.Amount_Per_Hour} onChange={handleChange} />
                            </div>
                            <div className="form-group" id="total_working_hours">
                              <label>Total Working Hours</label>
                              <input placeholder="Total Working Hours" name="Total_Working_Hours" id="total_working_hours2" type="text" className="form-control" value={formData.Total_Working_Hours} onChange={handleChange} />
                            </div>
                          </>
                        )}
                      </div>
                    </div>
                  </div>
                  <br />
                  <div className="row">
                    <div className="col">
                      <div className="form-group">
                        <label>Employee Number</label>
                        <input placeholder="Employee Number" name="Employee_Number" id="Employee_Number" type="text" className="form-control" onChange={handleChange} value={formData.Employee_Number} />
                      </div>
                      <div className="form-group">
                        <label>Designation</label>
                        <input placeholder="Designation" type="text" id="Designation" name="Designation" className="form-control" onChange={handleChange} value={formData.Designation} />
                      </div>
                      <div className="form-group">
                        <label>Location</label>
                        <input placeholder="Location" type="text" id="Location" name="Location" className="form-control" onChange={handleChange} value={formData.Location} />
                      </div>
                      <div className="form-group">
                        <label>Gender</label>
                        <select id="Gender" name="Gender" className="form-control" onChange={handleChange} value={formData.Gender}>
                          <option value="">--select--</option>
                          <option value="Male">Male</option>
                          <option value="Female">Female</option>
                        </select>
                      </div>
                    </div>
                    <div className="col">
                      <div className="form-group">
                        <label>DOB</label>
                        <input placeholder="DOB" type="date" id="DOB" name="DOB" className="form-control" onChange={handleChange} value={formData.DOB} />
                      </div>
                      <div className="form-group">
                        <label>Blood Group</label>
                        <input placeholder="Blood Group" type="text" id="Blood" name="Blood" className="form-control" onChange={handleChange} value={formData.Blood} />
                      </div>
                      <div className="form-group">
                        <label>Contact Number</label>
                        <input placeholder="Contact Number" type="text" id="Contact_Number" name="Contact_Number" className="form-control" onChange={handleChange} value={formData.Contact_Number} />
                      </div>
                      <div className="form-group">
                        <label>Emergency Contact Number</label>
                        <input placeholder="Emergency Contact Number" type="text" id="Emergency_Contact_Number" name="Emergency_Contact_Number" className="form-control" onChange={handleChange} value={formData.Emergency_Contact_Number} />
                      </div>
                    </div>
                  </div>
                  <br />
                  <div className="row">
                    <div className="col">
                      <div className="form-group">
                        <label>Personal Email</label>
                        <input placeholder="Personal Email" type="text" id="Personal_Email" name="Personal_Email" className="form-control" onChange={handleChange} value={formData.Personal_Email} />
                      </div>
                      <div className="form-group">
                        <label>Parent Name</label>
                        <input placeholder="Parent" type="text" id="Parent" name="Parent" className="form-control" onChange={handleChange} value={formData.Parent} />
                      </div>
                      <div className="form-group">
                        <label>Spouse Name</label>
                        <input placeholder="Spouse" type="text" id="Spouse" name="Spouse" className="form-control" onChange={handleChange} value={formData.Spouse} />
                      </div>
                    </div>
                    <div className="col">
                      <div className="form-group">
                        <label>Present Address</label>
                        <textarea placeholder="Address" type="text" id="Present_Address" name="Present_Address" className="form-control" onChange={(e) => handleAddressChange('Present_Address', e)} value={formData.Present_Address.address}></textarea>
                      </div>
                      <div className="form-group">
                        <input placeholder="City" type="text" id="city" name="city" className="form-control" onChange={(e) => handleAddressChange('Present_Address', e)} value={formData.Present_Address.city} />
                      </div>
                      <div className="form-group">
                        <input placeholder="State" type="text" id="state" name="state" className="form-control" onChange={(e) => handleAddressChange('Present_Address', e)} value={formData.Present_Address.state} />
                      </div>
                      <div className="form-group">
                        <input placeholder="Pincode" type="text" id="pincode" name="pincode" className="form-control" onChange={(e) => handleAddressChange('Present_Address', e)} value={formData.Present_Address.pincode} />
                      </div>
                      <div className="form-check">
                        <input className="form-check-input" type="checkbox" id="sameAddress" checked={sameAddress} onChange={handleSameAddressChange} />
                        <label className="form-check-label" htmlFor="sameAddress">
                          Same as Present Address
                        </label>
                      </div>
                    </div>
                  </div>
                  {!sameAddress && (
                    <>
                      <br />
                      <div className="row">
                        <div className="col">
                          <div className="form-group">
                            <label>Permanent Address</label>
                            <textarea placeholder="Address" type="text" id="Permanent_Address" name="Permanent_Address" className="form-control" onChange={(e) => handleAddressChange('Permanent_Address', e)} value={formData.Permanent_Address.address}></textarea>
                          </div>
                          <div className="form-group">
                            <input placeholder="City" type="text" id="city" name="city" className="form-control" onChange={(e) => handleAddressChange('Permanent_Address', e)} value={formData.Permanent_Address.city} />
                          </div>
                          <div className="form-group">
                            <input placeholder="State" type="text" id="state" name="state" className="form-control" onChange={(e) => handleAddressChange('Permanent_Address', e)} value={formData.Permanent_Address.state} />
                          </div>
                          <div className="form-group">
                            <input placeholder="Pincode" type="text" id="pincode" name="pincode" className="form-control" onChange={(e) => handleAddressChange('Permanent_Address', e)} value={formData.Permanent_Address.pincode} />
                          </div>
                        </div>
                      </div>
                    </>
                  )}
                  <br />
                  <div className="row">
                    <div className="col">
                      <div className="form-group">
                        <label>Bank Details</label>
                        <select id="Bank_Details" name="Bank_Details" className="form-control" onChange={(e) => setIsBankInfoVisible(e.target.value === 'Yes')} value={formData.Bank_Details}>
                          <option value="">--select--</option>
                          <option value="Yes">Yes</option>
                          <option value="No">No</option>
                        </select>
                      </div>
                    </div>
                  </div>
                  {isBankInfoVisible && (
                    <>
                      <div className="row">
                        <div className="col">
                          <div className="form-group">
                            <label>Account Number</label>
                            <input placeholder="Account Number" type="text" id="Account_Number" name="Account_Number" className="form-control" onChange={handleChange} value={formData.Account_Number} />
                          </div>
                          <div className="form-group">
                            <label>IFSC</label>
                            <input placeholder="IFSC" type="text" id="IFSC" name="IFSC" className="form-control" onChange={handleChange} value={formData.IFSC} />
                          </div>
                        </div>
                        <div className="col">
                          <div className="form-group">
                            <label>Bank Name</label>
                            <input placeholder="Bank Name" type="text" id="BankName" name="BankName" className="form-control" onChange={handleChange} value={formData.BankName} />
                          </div>
                          <div className="form-group">
                            <label>Branch Name</label>
                            <input placeholder="Branch Name" type="text" id="BranchName" name="BranchName" className="form-control" onChange={handleChange} value={formData.BranchName} />
                          </div>
                        </div>
                      </div>
                    </>
                  )}
                  <br />
                  <div className="row">
                    <div className="col text-center">
                      <button type="submit" className="btn btn-primary">Submit</button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </>
      );
    };

    export default App;
