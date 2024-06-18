import React, { useEffect, useState } from "react";
import FinBase from "../FinBase";
import { Link, useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import axios from "axios";
import config from "../../../functions/config";
import Swal from "sweetalert2";

const EmployeeForm = () => {

    const [sameAddress, setSameAddress] = useState(false);
    const [tdsApplicable, setTdsApplicable] = useState('');
    const [tdsType, setTdsType] = useState('');
    const [bloodGroup, setBloodGroup] = useState('');
    const [bankDetails, setBankDetails] = useState('');
    const [transactionType, setTransactionType] = useState('');
    const [age, setAge] = useState('');
    const [joiningDate, setJoiningDate] = useState('');
    const [isBankInfoVisible, setIsBankInfoVisible] = useState(false);
    const [isTdsInfoVisible, setIsTdsInfoVisible] = useState(false);
    const [isTdsPercentageVisible, setIsTdsPercentageVisible] = useState(false);
    const [isTdsAmountVisible, setIsTdsAmountVisible] = useState(false);
    const [salaryType, setSalaryType] = useState('');
    const [amountPerHour, setAmountPerHour] = useState(0);
    const [workingHours, setWorkingHours] = useState(0);
    const [salaryAmount, setSalaryAmount] = useState('');
    const [isPermanentAddressCopied, setIsPermanentAddressCopied] = useState(false);
    const [presentAddress, setPresentAddress] = useState({
      address: '',
      city: '',
      state: '',
      pincode: '',
    });
    const [permanentAddress, setPermanentAddress] = useState({
      address: '',
      city: '',
      state: '',
      pincode: '',
    });
  
    useEffect(() => {
      if (sameAddress) {
        setPermanentAddress({ ...presentAddress });
      }
    }, [sameAddress, presentAddress]);
  
    const handlePresentAddressChange = (e) => {
      const { name, value } = e.target;
      setPresentAddress((prev) => ({
        ...prev,
        [name]: value,
      }));
    };
  
    const handlePermanentAddressChange = (e) => {
      const { name, value } = e.target;
      setPermanentAddress((prev) => ({
        ...prev,
        [name]: value,
      }));
    };
  
    const handleSameAddressChange = () => {
      setSameAddress((prev) => !prev);
    };
  
  
    const handleSalaryTypeChange = (event) => {
      setSalaryType(event.target.value);
      // Reset the salary amount and other inputs when the salary type changes
      setSalaryAmount('');
      setAmountPerHour('');
      setWorkingHours('');
    };
    useEffect(() => {
        setJoiningDate(new Date().toISOString().split('T')[0]);
      }, []);
    
      useEffect(() => {
        if (bankDetails === 'Yes') {
          setIsBankInfoVisible(true);
        } else {
          setIsBankInfoVisible(false);
        }
      }, [bankDetails]);
    
      useEffect(() => {
        if (tdsApplicable === 'Yes') {
          setIsTdsInfoVisible(true);
        } else {
          setIsTdsInfoVisible(false);
        }
      }, [tdsApplicable]);
    
      useEffect(() => {
        if (tdsType === 'Percentage') {
          setIsTdsPercentageVisible(true);
          setIsTdsAmountVisible(false);
        } else if (tdsType === 'Amount') {
          setIsTdsPercentageVisible(false);
          setIsTdsAmountVisible(true);
        } else {
          setIsTdsPercentageVisible(false);
          setIsTdsAmountVisible(false);
        }
      }, [tdsType]);
    
      useEffect(() => {
        if (salaryType === 'Temporary' || salaryType === 'Fixed') {
          setSalaryAmount('');
        } else if (salaryType === 'Time Based') {
          calculateSalary();
        }
      }, [salaryType, amountPerHour, workingHours]);
    
      const calculateAge = (dob) => {
        const today = new Date();
        const birthDate = new Date(dob);
        let age = today.getFullYear() - birthDate.getFullYear();
        const monthDiff = today.getMonth() - birthDate.getMonth();
    
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
          age--;
        }
        return age;
      };
    
      const handleDOBChange = (e) => {
        const dob = e.target.value;
        setAge(calculateAge(dob));
      };
    
      const calculateSalary = () => {
        if (amountPerHour > 0 && workingHours > 0) {
          setSalaryAmount(amountPerHour * workingHours);
        } else {
          setSalaryAmount('');
        }
      };
  
    const handleAmountPerHourChange = (event) => {
      const value = event.target.value;
      setAmountPerHour(value);
      calculateAndSetSalary(value, workingHours);
    };
  
    const handleWorkingHoursChange = (event) => {
      const value = event.target.value;
      setWorkingHours(value);
      calculateAndSetSalary(amountPerHour, value);
    };
  
    const calculateAndSetSalary = (perHour, hours) => {
      const totalSalary = (parseFloat(perHour) || 0) * (parseFloat(hours) || 0);
      setSalaryAmount(totalSalary.toFixed(2));
    };
  
    const handleSalaryAmountChange = (event) => {
      if (salaryType !== 'Time Based') {
        setSalaryAmount(event.target.value);
      }
    };
  
   
    
    
  
   
  
    const handleBankDetailsChange = (e) => {
      setBankDetails(e.target.value);
    };
  
    const handleTdsApplicableChange = (e) => {
      setTdsApplicable(e.target.value);
    };
  
    const handleTdsTypeChange = (e) => {
      setTdsType(e.target.value);
    };
  
   
  
  return (
    <>
      <FinBase />
      <div
        className="page-content mt-0 pt-0"
        style={{ backgroundColor: "#2f516f", minHeight: "100vh" }}
      >
        <div className="d-flex justify-content-end mb-1">
          <Link to={"/items"}>
            <i
              className="fa fa-times-circle text-white mx-4 p-1"
              style={{ fontSize: "1.2rem", marginRight: "0rem !important" }}
            ></i>
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
            <div className="row">
              <div className="col-12 col-lg-12 col-xl-12"></div>
            </div>
            <form className="needs-validation px-1" validate>
              <br />
              <div className="row w-100">
                <div className="col-md-12 mx-0">
                    
                <div className="row">
            <div className="col-md-6">
                <div className="form-group">
                    <label>Title</label>
                    <select name="Title" className="form-control" required>
                        <option value="">--select--</option>
                        <option value="Mr">Mr</option>
                        <option value="Mrs">Mrs</option>
                        <option value="Miss">Miss</option>
                        <option value="Ms">Ms</option>
                    </select>
                </div>
                <div className="form-group">
                    <label>First Name</label>
                    <input placeholder="First Name" name="First_Name" type="text" className="form-control" />
                </div>
                <div className="form-group">
                    <label>Last Name</label>
                    <input placeholder="Last Name" name="Last_Name" type="text" className="form-control" />
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
                <input type="file" name="Image" id="Image" accept="image/*" style={{ display: 'none' }} />
            </div>

                   
                  </div>
                  <br />
                  
                  <div className="row">
                    <div className="col">
                      <div className="form-group">
                        <label>Alias (optional)</label>
                        <input placeholder="Alias" name="Alias" type="text" className="form-control" />
                      </div>
                      <div className="form-group">
                        <label>Date of Joining</label>
                        <input placeholder="Joining Date" required name="Joining_Date" id="JoiningDate" type="date" className="form-control" />
                      </div>
                    </div>
                    <div className="col">
                        
                      <div className="form-group">
                        <label>Salary Date</label>
                        <select className="form-control" name="Salary_Date">
                          <option value="">--select--</option>
                          <option value="1-10">1-10</option>
                          <option value="11-15">11-15</option>
                          <option value="16-31">16-31</option>
                        </select>
                      </div>
                      <div className="form-group">
      <label>Define salary details</label>
      <select
        className="form-control"
        name="Salary_Type"
        id="salary_type"
        onChange={handleSalaryTypeChange}
      >
        <option value="">--select--</option>
        <option value="Fixed">Fixed</option>
        <option value="Temporary">Temporary</option>
        <option value="Time Based">Time Based</option>
      </select>

      {(salaryType === 'Fixed' || salaryType === 'Temporary' || salaryType === 'Time Based') && (
        <div className="form-group" id="salary_amount">
          <label>Salary Amount</label>
          <input
            placeholder="Salary Amount"
            name="Salary_Amount"
            id="salary_amount2"
            type="text"
            className="form-control"
            value={salaryAmount}
            onChange={handleSalaryAmountChange}
            readOnly={salaryType === 'Time Based'}
          />
        </div>
      )}

      {salaryType === 'Time Based' && (
        <div id="salary_timebase">
          <div className="form-group">
            <label>Amount Per Hour</label>
            <input
              placeholder="Amount Per Hour"
              name="perhour"
             
              id="amount_perhour"
              type="number"
              className="form-control"
              value={amountPerHour}
            onChange={handleAmountPerHourChange}
            />
          </div>
          <div className="form-group">
            <label>Total Working Hour(s)</label>
            <input
              placeholder="Total Working Hour(s)"
              name="workhour"
              id="working_hours"
              type="number"
              className="form-control"
              value={workingHours}
            onChange={handleWorkingHoursChange}
            />
          </div>
        </div>
      )}
    </div>
  
                     
                     
                         
                    </div>
                  </div>
                  <br />
                  <center>
                    <p><b>General Information</b></p>
                  </center>
                  <div className="row">
                    <div className="form-group col">
                      <label>Employee Number</label>
                      <input placeholder="Employee Number" required name="Employee_Number" type="text" className="form-control" />
                    </div>
                    <div className="form-group col">
                      <label>Designation</label>
                      <input placeholder="Designation" name="Designation" type="text" className="form-control" />
                    </div>
                    <div className="form-group col">
                      <label>Location</label>
                      <input placeholder="Current Location" name="Location" type="text" className="form-control" />
                    </div>
                  </div>
                  <div className="row">
                    <div className="form-group col">
                      <label>Gender</label>
                      <select className="form-control" name="Gender" required>
                        <option value="">--select--</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Other">Other</option>
                      </select>
                    </div>
                    
                    <div className="form-group col">
                      <label>
                        Date Of Birth
                        <label className="ml-5 mr-1">Age</label>
                        </label>
                      <div className="row">
                        <div className="col-9">
                          <input
                            placeholder="Date Of Birth"
                            required
                            name="DOB"
                            id="DOB"
                            type="date"
                            className="form-control"
                            onChange={handleDOBChange}
                          />
                        </div>
                        <div className="col-3">
                          <input id="age" disabled className="form-control" type="text" readOnly value={age} />
                        </div>
                      </div>
                    </div>
                    <div className="form-group col">
                      <label>Blood Group</label>
                      <select className="form-control" name="Blood_Group">
                        <option value="">--select--</option>
                        <option value="A+">A+</option>
                        <option value="A-">A-</option>
                        <option value="B+">B+</option>
                        <option value="B-">B-</option>
                        <option value="AB+">AB+</option>
                        <option value="AB-">AB-</option>
                        <option value="O+">O+</option>
                        <option value="O-">O-</option>
                      </select>
                    </div>
                  </div>
                  <div className="row">
                  <div className="form-group col">
                      <label>Contact Number</label>
                      <input placeholder="Contact Number" name="Contact_Number" type="text" className="form-control" />
                    </div>
                    <div className="form-group col">
                      <label>Emergency Contact Number</label>
                      <input placeholder="Emergency Contact Number" name="Emergency_Contact_Number" type="text" className="form-control" />
                    </div>
                    <div className="form-group col">
                      <label> Email</label>
                      <input placeholder="Personal Email" required name="Personal_Email" type="email" className="form-control" />
                    </div>
                   
                    
                  </div>
                  <div className="row">
                   
                   
                    <div className="form-group col">
                      <label>Father's Name / Mother's Name</label>
                      <input placeholder="Father's Name / Mother's Name" name="Parent" type="text" className="form-control" />
                    </div>
                    <div className="form-group col">
                      <label>Spouse's Name</label>
                      <input placeholder="Spouse's Name" name="Spouse" type="text" className="form-control" />
                    </div>
                    <div className="form-group col">
                      <label>File</label>
                      <input name="File" type="file" class="form-control"/>                    
                      </div>
                  </div>
                  <br />
                  <div className="row">
                    <div className="form-group col">
                    <label>Provide bank Details</label>
                    <select className="form-control" name="Bank_Details" value={bankDetails} onChange={(e) => setBankDetails(e.target.value)}>
                        <option value="">--select--</option>
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                    </div>

                    <div className="form-group col">
                    <label>TDS Applicable</label>
                    <select className="form-control" name="tds_applicable" value={tdsApplicable} onChange={(e) => setTdsApplicable(e.target.value)}>
                        <option value="">--select--</option>
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                    </div>
                </div>
                {isBankInfoVisible && (
        <div className="row">
          <div className="form-group col" id="BankInfo">
            <center>
              <p><b>Banking Information</b></p>
            </center>
            <div>
              <label>Account Number</label>
              <input placeholder="Account Number" name="Account_Number" type="text" className="form-control" />
            </div>
            <div>
              <label>IFSC</label>
              <input placeholder="SBIN0071242" pattern="^[A-Za-z]{4}0[A-Za-z0-9]{6}$" name="IFSC" type="text" className="form-control" />
            </div>
            <div>
              <label>Name of Bank</label>
              <input placeholder="Name Of Bank" name="BankName" type="text" className="form-control" />
            </div>
            <div>
              <label>Branch Name</label>
              <input placeholder="Branch Name" name="BranchName" type="text" className="form-control" />
            </div>
            <center>
              <p><b>For Banking</b></p>
            </center>
            <div>
              <label>Transaction Type</label>
              <select className="form-control" name="Transaction_Type" value={transactionType} onChange={(e) => setTransactionType(e.target.value)}>
                <option value="">--select--</option>
                <option value="ATM">ATM</option>
                <option value="Cash">Cash</option>
                <option value="Cheque">Cheque</option>
              </select>
            </div>
          </div>
        </div>
      )}

      {isTdsInfoVisible && (
        <div className="row">
          <div className="form-group col" id="TDSinfo">
            <center>
              <p><b>TDS Application</b></p>
            </center>
            <div>
              <label>Percentage/Amount</label>
              <select className="form-control" id="TDStype" name="TDS_Type" value={tdsType} onChange={(e) => setTdsType(e.target.value)}>
                <option value="">--select--</option>
                <option value="Percentage">Percentage</option>
                <option value="Amount">Amount</option>
              </select>
            </div>

            {isTdsPercentageVisible && (
              <div id="TDSpercentage">
                <label>Enter TDS Percentage</label>
                <input placeholder="TDS Percentage" name="TDS_Percentage" type="text" className="form-control" />
              </div>
            )}

            {isTdsAmountVisible && (
              <div id="TDSamount">
                <label>Enter TDS Amount</label>
                <input placeholder="TDS Amount" name="TDS_Amount" type="text" className="form-control" />
              </div>
            )}
          </div>
        </div>
      )}

                 <br></br>
                  <center>
                    <p><b>Address Details</b></p>
                  </center>
                  
                  <br />
      <center>
        <p><b>Address Details</b></p>
      </center>
      <div className="row">
        <div className="col-md-6">
          <div className="form-group">
            <label>Present Address</label>
            <textarea
              placeholder="Present Address"
              name="address"
              className="form-control"
              rows="3"
              value={presentAddress.address}
              onChange={handlePresentAddressChange}
            ></textarea>
          </div>
          <div className="form-group">
            <label>Present City</label>
            <input
              placeholder="Present City"
              name="city"
              type="text"
              className="form-control"
              value={presentAddress.city}
              onChange={handlePresentAddressChange}
            />
          </div>
          <div className="form-group">
            <label>Present State</label>
            <input
              placeholder="Present State"
              name="state"
              type="text"
              className="form-control"
              value={presentAddress.state}
              onChange={handlePresentAddressChange}
            />
          </div>
          <div className="form-group">
            <label>Present Pincode</label>
            <input
              placeholder="Present Pincode"
              name="pincode"
              type="text"
              className="form-control"
              value={presentAddress.pincode}
              onChange={handlePresentAddressChange}
            />
          </div>
        </div>
        <div className="col-md-6">
          <div className="form-group">
            <label>
              Permanent Address
              <input
                type="checkbox"
                id="sameAddress"
                checked={sameAddress}
                onChange={handleSameAddressChange}
                className="ml-2"
              />
              <small className="ml-1">Same as Present Address</small>
            </label>
            <textarea
              placeholder="Permanent Address"
              name="address"
              className="form-control"
              rows="3"
              value={permanentAddress.address}
              onChange={handlePermanentAddressChange}
              disabled={sameAddress}
            ></textarea>
          </div>
          <div className="form-group">
            <label>Permanent City</label>
            <input
              placeholder="Permanent City"
              name="city"
              type="text"
              className="form-control"
              value={permanentAddress.city}
              onChange={handlePermanentAddressChange}
              disabled={sameAddress}
            />
          </div>
          <div className="form-group">
            <label>Permanent State</label>
            <input
              placeholder="Permanent State"
              name="state"
              type="text"
              className="form-control"
              value={permanentAddress.state}
              onChange={handlePermanentAddressChange}
              disabled={sameAddress}
            />
          </div>
          <div className="form-group">
            <label>Permanent Pincode</label>
            <input
              placeholder="Permanent Pincode"
              name="pincode"
              type="text"
              className="form-control"
              value={permanentAddress.pincode}
              onChange={handlePermanentAddressChange}
              disabled={sameAddress}
            />
          </div>
        </div>
      </div>
    
  

                  <br />
                  <center>
        <p><b>Statutory Information</b></p>
      </center>
      <div className="row">
        <div className="col">
          <div>
            <label>Income Tax Number</label>
            <input placeholder="Income Tax Number" name="Income_Tax" type="text" className="form-control" />
          </div>
          <div>
            <label>Aadhar Number</label>
            <input name="Aadhar" placeholder="12 Digit Unique Number" maxLength="14" pattern="\d{4} \d{4} \d{4}" type="text" className="form-control" />
          </div>
          <div>
            <label>Universal Account Number (UAN)</label>
            <input placeholder="12 digit number" pattern="\d{12}" maxLength="12" name="UAN" type="text" className="form-control" />
          </div>
        </div>
        <div className="col">
          <div>
            <label>PF Account Number</label>
            <input placeholder="MH/PUN/1234567/12" name="PF" pattern="[A-Z]{2}/[A-Z0-9]{3}/[0-9]{7}/[0-9]{0,2}" type="text" className="form-control" />
          </div>
          <div>
            <label>PAN Number</label>
            <input placeholder="ABCDE1234F" name="PAN" pattern="[A-Z]{5}[0-9]{4}[A-Z]" maxLength="10" type="text" className="form-control" />
          </div>
          <div>
            <label>PR Account Number</label>
            <input placeholder="12 digit number" pattern="\d{12}" name="PR" type="text" className="form-control" />
          </div>
        </div>
      </div>
      <center>

      <div className="row mt-5 mb-5">
        <div className="col-md-4"></div>
        <div className="col-md-4 d-flex justify-content-center">
          <button className="btn btn-outline-secondary w-50 text-light" type="submit">
            SAVE
          </button>
          <a href="/employee_list" className="btn btn-outline-secondary w-25 ml-1 text-light">
            CANCEL
          </a>
        </div>
        <div className="col-md-4"></div>
      </div>
                  </center>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default EmployeeForm;
